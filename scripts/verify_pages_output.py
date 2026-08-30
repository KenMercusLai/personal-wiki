from __future__ import annotations

import html
import json
import pathlib
import re
import sys
from html.parser import HTMLParser
from urllib.parse import unquote, urlsplit

REPOSITORY_ROOT = pathlib.Path(__file__).resolve().parents[1]
if str(REPOSITORY_ROOT) not in sys.path:
    sys.path.insert(0, str(REPOSITORY_ROOT))

from tools.validate_publish import ValidationError, validate_publish

BASE_EXPECTED = {
    "index.html",
    "wiki/index.html",
    "wiki/sources/index.html",
    "wiki/concepts/index.html",
    "wiki/entities/index.html",
    "sitemap.xml",
    "robots.txt",
}

SOURCE_CONTRACTS = {
    "wei-jie-pun-translation-woman-communication": {
        "derived": {
            "wiki/concepts/semantic-retrieval-for-pun-translation/index.html",
            "wiki/concepts/functional-equivalence-in-pun-localization/index.html",
            "wiki/concepts/weak-guidance-in-game-localization/index.html",
            "wiki/entities/woman-communication/index.html",
            "wiki/entities/wei-jie/index.html",
        },
        "images": {
            "semantic-search-candidates.png": "程序输出展示语义相近的谐音候选",
            "localized-character-name.png": "《女性交流》中文本地化后的角色姓名示例",
            "weak-guidance-japanese.png": "日文画面标出やりチン与チンゲ的重叠部分",
            "weak-guidance-chinese.jpg": "中文画面标出口鲍与鲍鱼的重叠部分",
        },
        "phrases": {
            "语义检索辅助谐音梗翻译",
            "功能对等与游戏本地化",
            "游戏文本中的弱引导",
            "本次图文Ingest已完整读取并检查15个原始图片引用",
            "精选4张公开嵌入",
            "另外11张不嵌入是编辑选择，不代表private分类",
        },
    },
    "shensiquan-private-data-chatgpt-langchain": {
        "derived": {
            "wiki/concepts/retrieval-augmented-generation-pipeline/index.html",
            "wiki/concepts/document-chunking-retrieval-tradeoff/index.html",
            "wiki/entities/langchain/index.html",
        },
        "images": {
            "rag-query-flow.png": "带聊天历史与向量检索的问答流程",
            "document-embedding-vectorstore.png": "文档切片、生成嵌入并写入向量库的流程",
            "generative-ai-stack.jpg": "生成式人工智能技术栈中的模型、框架与应用层",
        },
        "phrases": {
            "原文处于GPT-4发布和LangChain早期发展的时间窗口",
            "本次图文Ingest完整读取并检查17个原始图片引用",
            "精选3张能解释数据摄取、查询检索和应用技术栈的图片公开嵌入",
            "其余14张多为操作界面、产品截图、增长图、推广图或往期文章封面",
            "并非private处理",
        },
    },
    "chen-hao-http-history": {
        "derived": {
            "wiki/concepts/http-version-evolution/index.html",
            "wiki/concepts/http-head-of-line-blocking/index.html",
            "wiki/entities/quic/index.html",
        },
        "images": {},
        "phrases": {
            "HTTP版本演进",
            "队头阻塞",
            "2019年的协议生态快照",
            "原文没有图片引用",
            "RFC 9114",
        },
    },
    "spacewander-ai-inference-load-balancing": {
        "derived": {
            "wiki/concepts/inference-load-balancer-design/index.html",
            "wiki/concepts/kv-cache-aware-routing/index.html",
            "wiki/concepts/distributed-scheduler-state-collection/index.html",
        },
        "images": {},
        "phrases": {
            "推理负载均衡器",
            "Tokenization",
            "KV Cache",
            "O(n²)",
            "原文没有图片引用",
            "作者评价与可复核事实",
        },
    },
    "matianjiangxin-douglas-peucker-trajectory-simplification": {
        "derived": {
            "wiki/concepts/ramer-douglas-peucker-algorithm/index.html",
            "wiki/concepts/geospatial-simplification-tolerance/index.html",
        },
        "images": {
            "douglas-peucker-simplification.gif": "道格拉斯-普克算法递归保留关键点的示意动画",
            "trajectory-original.png": "抽稀前由812个采样点构成的车辆轨迹",
            "trajectory-epsilon-0-001.png": "epsilon为0.001时由35个点近似的车辆轨迹",
        },
        "phrases": {
            "Ramer–Douglas–Peucker",
            "812个轨迹点",
            "35个点",
            "坐标系与距离单位",
            "精选3张公开嵌入",
            "3张因信息重复而省略",
        },
    },
    "indigo-feynman-information-knowledge-output": {
        "derived": {
            "wiki/concepts/explanation-driven-learning-loop/index.html",
            "wiki/concepts/topic-driven-reading-and-output/index.html",
            "wiki/concepts/ai-assisted-note-retrieval/index.html",
        },
        "images": {
            "feynman-learning-cycle.png": "目标、理解、输出、回顾与内化组成的费曼学习循环",
            "information-to-knowledge-output.png": "从随机阅读和聚焦阅读到笔记、长文与课程输出的流程",
            "structured-output-workflow.png": "围绕主题页面完成精读、研究、长文和课程输出的工作流",
        },
        "phrases": {
            "解释驱动学习",
            "随机漫步",
            "聚焦阅读",
            "Dale",
            "9张原始图片引用已解析",
            "6张省略",
        },
    },
    "piotr-wozniak-goals-and-learn-drive": {
        "derived": {
            "wiki/concepts/goals-as-attentional-valuation/index.html",
            "wiki/concepts/small-step-interest-cultivation/index.html",
        },
        "images": {},
        "phrases": {
            "目标作为注意力与知识估值中心",
            "学习内驱力",
            "5–10分钟",
            "作者观点与证据边界",
            "原文没有图片引用",
        },
    },
    "bernard-marr-timeless-productivity-habits": {
        "derived": {
            "wiki/concepts/attention-protection-work-design/index.html",
            "wiki/concepts/task-prioritization-and-batching/index.html",
            "wiki/concepts/workload-reduction-by-elimination-automation-delegation/index.html",
        },
        "images": {},
        "phrases": {
            "3至5件",
            "不紧急但重要",
            "上下文切换",
            "删除、自动化与委派",
            "2014年的工具生态",
            "原文没有图片引用",
        },
    },
    "tuimo-gpv-career-path": {
        "derived": {
            "wiki/concepts/gpv-career-hypothesis/index.html",
            "wiki/concepts/career-path-not-job-title/index.html",
        },
        "images": {},
        "phrases": {
            "Gifts、Passion与Values",
            "职业假设",
            "职业生涯不等于单一工作",
            "市场需求与现实约束",
            "原文没有图片引用",
        },
    },
    "yuan-chaofa-agentic-rag-evolution": {
        "derived": {
            "wiki/concepts/agentic-rag-control-loop/index.html",
            "wiki/concepts/coarse-to-fine-evidence-retrieval/index.html",
            "wiki/concepts/search-policy-learning/index.html",
        },
        "images": {
            "native-rag-offline-online.png": "传统RAG的离线入库与在线检索生成链路",
            "agentic-rag-tool-loop.png": "模型按需调用搜索工具并根据结果继续决策的Agentic RAG循环",
            "chatbox-agentic-search-flow.png": "Chatbox在普通检索与多轮Agentic Search之间选择的流程",
            "search-r1-reason-search-loop.png": "Search-R1在推理中决定搜索、接收结果并继续推理的循环",
        },
        "phrases": {
            "检索策略控制器",
            "先粗后细",
            "Search-R1",
            "示意代码不能视为可运行训练实现",
            "精选4张公开嵌入",
            "3张省略",
        },
    },
    "piotr-wozniak-mechanics-of-eustress": {
        "derived": {
            "wiki/concepts/challenge-reward-control-balance/index.html",
            "wiki/concepts/acute-chronic-stress-boundary/index.html",
        },
        "images": {
            "problem-difficulty-expected-reward.png": "问题难度、成功概率、奖励与期望收益之间的示意关系",
        },
        "phrases": {
            "自主性、可控性与恢复",
            "急性挑战与慢性压力",
            "示意模型而非实测曲线",
            "不构成医学建议",
            "1个原始图片引用已解析并公开嵌入",
        },
    },
    "program-think-systematic-learning": {
        "derived": {
            "wiki/concepts/systematic-learning-breadth-depth/index.html",
            "wiki/concepts/dikw-as-information-transformation-model/index.html",
            "wiki/concepts/explanation-driven-learning-loop/index.html",
        },
        "images": {},
        "phrases": {
            "广度、深度与依赖顺序",
            "媒介适配",
            "DIKW",
            "描述性框架而非公认定律",
            "熵的跨领域类比",
            "原文没有图片引用",
        },
    },
    "hulatu-forward-reference-learning-friction": {
        "derived": {
            "wiki/concepts/learning-with-unresolved-dependencies/index.html",
            "wiki/concepts/systematic-learning-breadth-depth/index.html",
        },
        "images": {},
        "phrases": {
            "未解析知识依赖",
            "编程术语与学习类比",
            "全局地图",
            "局部回补",
            "死记硬背",
            "2张全部解析",
        },
    },
    "hutusi-silver-bullet-software-engineering-history": {
        "derived": {
            "wiki/concepts/essential-and-accidental-software-work/index.html",
            "wiki/concepts/ai-assisted-software-development-verification-loop/index.html",
        },
        "images": {
            "fred-brooks-mythical-man-month.jpg": "弗雷德·布鲁克斯演讲照片与《人月神话》封面的组合图",
        },
        "phrases": {
            "本质性工作与附属性工作",
            "软件工程历史",
            "LLM是银弹",
            "2024年的预测",
            "历史校正",
            "5张全部解析",
        },
    },
    "yuanming-hu-ten-claude-code-agents": {
        "derived": {
            "wiki/concepts/parallel-coding-agent-worktree-orchestration/index.html",
            "wiki/concepts/agent-operational-memory/index.html",
            "wiki/concepts/ai-assisted-software-development-verification-loop/index.html",
        },
        "images": {
            "worktree-parallel-agent-architecture.png": "用独立Git worktree运行多个编码代理并共享任务状态的架构图",
        },
        "phrases": {
            "并行代理吞吐",
            "权限与隔离边界",
            "Git worktree",
            "结构化日志",
            "标准化软件的终结",
            "不晚于2026-02-15",
            "12张全部解析",
        },
    },
}

EXPECTED = set(BASE_EXPECTED)
for source_key, contract in SOURCE_CONTRACTS.items():
    bundle = f"wiki/sources/{source_key}"
    EXPECTED.add(f"{bundle}/index.html")
    EXPECTED.update(f"{bundle}/{filename}" for filename in contract["images"])
    EXPECTED.update(contract["derived"])


def dynamic_expected_artifacts(repository: pathlib.Path | str) -> set[str]:
    """Derive the complete public contract from the current validated canonical tree."""
    report = validate_publish(repository)
    route_artifacts = {f"{route.rstrip('/')}/index.html" for route in report.routes}
    return route_artifacts | set(report.assets)

PRIVATE_PATH_PATTERNS = (
    re.compile(r"(?i)(?:file:/+)?/Users/[^/\s<>\"']+/"),
    re.compile(r"(?i)(?:file:/+)?/home/[^/\s<>\"']+/"),
    re.compile(r"(?i)(?:file:/+)?[a-z]:[\\/]+Users[\\/]+[^\\/\s<>\"']+[\\/]"),
    re.compile(r"(?i)(?:^|[\s=\"'(:])~/"),
)
PRIVATE_PATH_MARKERS = (
    "com~apple~CloudDocs",
    "Mobile Documents/com~apple~CloudDocs",
    "98. static/img",
)
PRIVATE_DIRECTORY_NAMES = {"raw", "inbox", "archive", "metadata"}
RAW_IMAGE_SUFFIXES = {".gif", ".jpeg", ".jpg", ".png", ".svg", ".webp"}
GENERATED_TEXT_SUFFIXES = {
    ".css",
    ".csv",
    ".html",
    ".js",
    ".json",
    ".map",
    ".md",
    ".svg",
    ".txt",
    ".webmanifest",
    ".xml",
}
HTTP_URL_PATTERN = re.compile(r"(?i)https?://[^\s<>\"'\[\](){};,!，；！]+")
MAX_DECODE_PASSES = 16


def without_http_url_paths(text: str) -> str:
    query_and_fragment = []

    def replace(match: re.Match[str]) -> str:
        parsed = urlsplit(match.group(0))
        query_and_fragment.extend((parsed.query, parsed.fragment))
        return " "

    remaining = HTTP_URL_PATTERN.sub(replace, text)
    return " ".join((remaining, *query_and_fragment))


def find_private_path_leaks(text: str) -> list[str]:
    normalized = text
    decode_limit_reached = False
    for _ in range(MAX_DECODE_PASSES):
        decoded = unquote(html.unescape(normalized))
        if decoded == normalized:
            break
        normalized = decoded
    else:
        decode_limit_reached = True

    filesystem_text = without_http_url_paths(normalized)
    leaks = [
        match.group(0)
        for pattern in PRIVATE_PATH_PATTERNS
        for match in pattern.finditer(filesystem_text)
    ]
    leaks.extend(
        marker
        for marker in PRIVATE_PATH_MARKERS
        if marker.casefold() in filesystem_text.casefold()
    )
    if decode_limit_reached:
        leaks.append("excessive nested URL/HTML encoding")
    return sorted(set(leaks))


def find_private_path_leaks_in_bytes(raw: bytes) -> list[str]:
    text = raw.decode("utf-8", errors="replace")
    return find_private_path_leaks(text)


def is_generated_text_artifact(path: pathlib.Path) -> bool:
    return path.suffix.casefold() in GENERATED_TEXT_SUFFIXES


def find_forbidden_public_files(paths: list[str]) -> list[str]:
    forbidden = []
    for raw_path in paths:
        path = pathlib.PurePosixPath(raw_path)
        parts = {part.casefold() for part in path.parts}
        name = path.name.casefold()
        if parts & PRIVATE_DIRECTORY_NAMES:
            forbidden.append(raw_path)
        elif name in {"asset-manifest.json", "source.original.md", "source-registry.json"}:
            forbidden.append(raw_path)
        elif path.suffix.casefold() in RAW_IMAGE_SUFFIXES and "_md5" in name:
            forbidden.append(raw_path)
    return forbidden


def find_external_image_sources(images: list[tuple[str, str]]) -> list[str]:
    external: list[str] = []
    for src, _alt in images:
        parsed = urlsplit(html.unescape(src))
        if parsed.scheme or parsed.netloc:
            external.append(src)
    return external


class PageParser(HTMLParser):
    def __init__(self):
        super().__init__(convert_charrefs=True)
        self.canonical: list[str] = []
        self.links: list[str] = []
        self.images: list[tuple[str, str]] = []
        self.jsonld: list[str] = []
        self._json = False
        self._buffer: list[str] = []

    def handle_starttag(self, tag, attrs):
        values = dict(attrs)
        rel = values.get("rel") or ""
        href = values.get("href") or ""
        if tag == "link" and "canonical" in rel.split():
            self.canonical.append(href)
        if tag == "a" and href:
            self.links.append(href)
        src = values.get("src")
        if tag == "img" and isinstance(src, str):
            self.images.append((src, values.get("alt") or ""))
        if tag == "script" and values.get("type") == "application/ld+json":
            self._json = True
            self._buffer = []

    def handle_data(self, data):
        if self._json:
            self._buffer.append(data)

    def handle_endtag(self, tag):
        if tag == "script" and self._json:
            self.jsonld.append("".join(self._buffer))
            self._json = False


def main() -> int:
    public = pathlib.Path(sys.argv[1] if len(sys.argv) > 1 else "public").resolve()
    errors: list[str] = []
    try:
        current_expected = dynamic_expected_artifacts(REPOSITORY_ROOT)
    except ValidationError as exc:
        print(f"Generated-site verification failed:\n- canonical contract invalid: {exc}")
        return 1
    required = EXPECTED | current_expected
    for rel in required:
        if not (public / rel).is_file():
            errors.append(f"missing artifact: {rel}")

    html_files = sorted(public.rglob("*.html"))
    if not html_files:
        errors.append("no HTML files generated")
    expected_wiki_html = {rel for rel in current_expected if rel.endswith(".html")}
    actual_wiki_html = {
        path.relative_to(public).as_posix()
        for path in html_files
        if path.relative_to(public).parts[:1] == ("wiki",)
    }
    for rel in sorted(actual_wiki_html - expected_wiki_html):
        errors.append(f"unexpected canonical wiki route artifact: {rel}")

    parsed_pages: dict[pathlib.Path, PageParser] = {}
    for path in html_files:
        text = path.read_text(encoding="utf-8")
        parser = PageParser()
        parser.feed(text)
        parsed_pages[path] = parser
        rel = path.relative_to(public)
        if len(parser.canonical) != 1:
            errors.append(f"{rel}: expected one canonical, found {len(parser.canonical)}")
        if len(parser.jsonld) != 1:
            errors.append(f"{rel}: expected one JSON-LD block, found {len(parser.jsonld)}")
        for payload in parser.jsonld:
            try:
                data = json.loads(payload)
            except json.JSONDecodeError as exc:
                errors.append(f"{rel}: invalid JSON-LD: {exc}")
                continue
            if parser.canonical and data.get("url") != parser.canonical[0]:
                errors.append(f"{rel}: JSON-LD URL differs from canonical")
        if "![[" in text:
            errors.append(f"{rel}: unresolved private image reference leaked into HTML")
        for src in find_external_image_sources(parser.images):
            errors.append(f"{rel}: external image source is forbidden: {src}")

    for path in sorted(
        item
        for item in public.rglob("*")
        if item.is_file() and is_generated_text_artifact(item)
    ):
        try:
            raw = path.read_bytes()
        except OSError:
            continue
        rel = path.relative_to(public)
        for leak in find_private_path_leaks_in_bytes(raw):
            errors.append(f"{rel}: private source path leaked into generated text: {leak}")

    if parsed_pages:
        root = parsed_pages.get(public / "index.html")
        if root and root.canonical:
            base = root.canonical[0]
            base_parts = urlsplit(base)
            prefix = base_parts.path.rstrip("/") + "/"
            for path, parser in parsed_pages.items():
                rel = path.relative_to(public)
                if parser.canonical:
                    canonical = urlsplit(parser.canonical[0])
                    if (canonical.scheme, canonical.netloc) != (base_parts.scheme, base_parts.netloc):
                        errors.append(f"{rel}: canonical origin mismatch")
                    if not canonical.path.startswith(prefix):
                        errors.append(f"{rel}: canonical escapes project prefix {prefix}")
                for href in parser.links:
                    target = urlsplit(html.unescape(href))
                    if target.scheme or target.netloc or href.startswith("#") or href.startswith("mailto:"):
                        continue
                    decoded = unquote(target.path)
                    if not decoded.startswith(prefix):
                        errors.append(f"{rel}: internal link escapes project prefix: {href}")
                        continue
                    local = decoded[len(prefix):]
                    candidate = public / local
                    if local.endswith("/"):
                        candidate = candidate / "index.html"
                    if not candidate.exists():
                        errors.append(f"{rel}: broken internal link: {href}")

    for source_key, contract in SOURCE_CONTRACTS.items():
        rel = pathlib.Path(f"wiki/sources/{source_key}/index.html")
        source_html = public / rel
        if not source_html.is_file():
            continue
        rendered = source_html.read_text(encoding="utf-8")
        parser = parsed_pages[source_html]
        for phrase in contract["phrases"]:
            if phrase not in rendered:
                errors.append(f"{rel}: missing expected text: {phrase}")
        for filename, expected_alt in contract["images"].items():
            matching = [
                alt
                for src, alt in parser.images
                if (
                    urlsplit(src).path == filename
                    or urlsplit(src).path.endswith(f"/{filename}")
                )
            ]
            if not matching:
                errors.append(f"{rel}: missing selected image src: {filename}")
            elif matching != [expected_alt]:
                errors.append(f"{rel}: unexpected alt text for {filename}: {matching}")

    if errors:
        print("Generated-site verification failed:")
        for error in errors:
            print(f"- {error}")
        return 1
    print(f"Verified {len(html_files)} HTML pages and {len(required)} required baseline + dynamic artifacts.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
