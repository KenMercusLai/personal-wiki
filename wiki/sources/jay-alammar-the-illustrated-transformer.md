---
title: "The Illustrated Transformer"
type: source
tags: [transformer, attention, deep-learning, nlp, machine-translation]
date: 2018-06-27
source_file: "/mnt/ken_personal_wiki/Articles/Jay Alammar - The Illustrated Transformer.md"
---

## Summary
[[JayAlammar]] gives a visual, deliberately simplified walkthrough of the encoder-decoder Transformer introduced by “Attention Is All You Need,” using machine translation to connect the full architecture to [[AttentionMechanism|scaled dot-product attention]], multi-head attention, [[PositionalEncoding]], autoregressive decoding, and training targets. The article's diagrams expose the flow from word embeddings through stacked residual attention and feed-forward blocks to vocabulary probabilities, while its worked numbers are pedagogical examples rather than measurements. It is a strong account of the original 2017 architecture, not a survey of later decoder-only language models or newer attention and position variants.

![Black-box Transformer translating the French sentence Je suis étudiant into I am a student](../../wiki-assets/jay-alammar-the-illustrated-transformer/transformer-translation-black-box.png)

## Key Claims
- The original [[TransformerArchitecture]] is an encoder-decoder system: the encoder stack turns the entire input into contextual vectors, and every decoder layer can attend to that encoded representation while generating the output.

![Transformer overview with an encoder component feeding a decoder component](../../wiki-assets/jay-alammar-the-illustrated-transformer/encoder-decoder-overview.png)

![Six encoders stacked beside six decoders with every decoder receiving the top encoder output](../../wiki-assets/jay-alammar-the-illustrated-transformer/six-layer-encoder-decoder-stacks.png)

- Each encoder layer applies self-attention and then the same feed-forward network independently at every position. Each decoder layer adds encoder-decoder cross-attention between masked self-attention and its feed-forward network.

![Encoder layer with self-attention followed by a feed-forward neural network](../../wiki-assets/jay-alammar-the-illustrated-transformer/encoder-self-attention-feed-forward.png)

![Decoder layer adding encoder-decoder attention between self-attention and feed-forward sublayers](../../wiki-assets/jay-alammar-the-illustrated-transformer/decoder-with-cross-attention.png)

- Input words first become vectors; in the paper's base configuration these have width 512. Self-attention couples token paths, while the positionwise feed-forward computation can run across positions in parallel.

![French input words represented as separate embedding vectors](../../wiki-assets/jay-alammar-the-illustrated-transformer/input-word-embeddings.png)

![Three token vectors sharing self-attention and then following parallel feed-forward paths](../../wiki-assets/jay-alammar-the-illustrated-transformer/parallel-token-paths-through-encoder.png)

![Thinking and Machines token vectors passing through shared self-attention and separate positionwise feed-forward networks](../../wiki-assets/jay-alammar-the-illustrated-transformer/self-attention-then-positionwise-feed-forward.png)

- Self-attention contextualizes a position by giving relevant positions more weight. The pronoun example visualizes “it” attending to “animal,” but the picture illustrates a learned association rather than proving linguistic understanding.

![Attention visualization showing the pronoun it attending strongly to the animal](../../wiki-assets/jay-alammar-the-illustrated-transformer/pronoun-attention-to-animal.png)

- Scaled dot-product attention projects each input into query, key, and value vectors. Query-key dot products are divided by the square root of key width, normalized with softmax, and used to weight a sum of value vectors.

![Word embeddings projected into query key and value vectors by three learned weight matrices](../../wiki-assets/jay-alammar-the-illustrated-transformer/query-key-value-projections.png)

![Query for Thinking dotted with the keys for Thinking and Machines to produce attention scores](../../wiki-assets/jay-alammar-the-illustrated-transformer/query-key-dot-product-scores.png)

![Attention scores divided by the square root of key dimension and normalized to 0.88 and 0.12](../../wiki-assets/jay-alammar-the-illustrated-transformer/scaled-softmax-attention-weights.png)

![Softmax weights scaling value vectors before their sum forms the attention output](../../wiki-assets/jay-alammar-the-illustrated-transformer/weighted-values-and-summed-output.png)

- The same calculation is performed efficiently with matrices: `Q = XWQ`, `K = XWK`, and `V = XWV`, followed by `softmax(QKᵀ / √dₖ)V`.

![Input matrix X multiplied by learned query key and value weight matrices](../../wiki-assets/jay-alammar-the-illustrated-transformer/matrix-qkv-projections.png)

![Scaled dot-product attention formula softmax of Q times K transpose over square root of key dimension multiplied by V](../../wiki-assets/jay-alammar-the-illustrated-transformer/scaled-dot-product-attention-formula.png)

- Multi-head attention repeats that computation with independent learned projections, allowing different representation subspaces and attention patterns. The base model uses eight heads, concatenates their outputs, and applies a learned output projection before the feed-forward network.

![Two attention heads using independent query key and value projection matrices](../../wiki-assets/jay-alammar-the-illustrated-transformer/two-attention-head-projections.png)

![Eight attention heads independently producing output matrices from the same input](../../wiki-assets/jay-alammar-the-illustrated-transformer/eight-attention-head-outputs.png)

![Eight attention-head outputs concatenated and multiplied by an output weight matrix](../../wiki-assets/jay-alammar-the-illustrated-transformer/concatenate-heads-output-projection.png)

![Five-stage multi-head attention workflow from token embeddings through eight heads to one output matrix](../../wiki-assets/jay-alammar-the-illustrated-transformer/multi-head-attention-workflow.png)

- Different heads can emphasize different relations: in the example, two heads connect “it” most strongly with “animal” and “tired,” while viewing all heads together is visibly harder to interpret.

![Two attention heads linking it most strongly to animal and tired](../../wiki-assets/jay-alammar-the-illustrated-transformer/two-head-pronoun-attention.png)

![All attention heads shown simultaneously for the token it in the example sentence](../../wiki-assets/jay-alammar-the-illustrated-transformer/all-heads-pronoun-attention.png)

- Because attention alone does not encode sequence order, the model adds a deterministic position vector to each token embedding. The article distinguishes an older Tensor2Tensor visualization that concatenates sine and cosine halves from the paper's interleaved sine/cosine dimensions.

![Positional encoding vectors added to token embeddings before the encoder stack](../../wiki-assets/jay-alammar-the-illustrated-transformer/token-and-positional-embedding-addition.png)

![Toy four-dimensional positional encodings added to three French word embeddings](../../wiki-assets/jay-alammar-the-illustrated-transformer/toy-positional-encoding-values.png)

![Heatmap of 20 positional encodings with concatenated sine and cosine halves across 512 dimensions](../../wiki-assets/jay-alammar-the-illustrated-transformer/concatenated-sine-cosine-position-heatmap.png)

![Heatmap of interleaved sine and cosine positional encodings by token position and embedding dimension](../../wiki-assets/jay-alammar-the-illustrated-transformer/interleaved-sine-cosine-position-heatmap.png)

- Residual connections wrap every attention and feed-forward sublayer, followed in the illustrated original design by layer normalization. The complete diagrams show these paths in both stacks and the encoder output feeding decoder cross-attention.

![Encoder showing residual paths around self-attention and feed-forward sublayers followed by add and normalize](../../wiki-assets/jay-alammar-the-illustrated-transformer/encoder-residual-add-normalize.png)

![Encoder detail showing layer normalization applied to an input vector plus its self-attention output](../../wiki-assets/jay-alammar-the-illustrated-transformer/encoder-layer-normalization-equation.png)

![Two-layer Transformer with residual encoder and decoder sublayers cross-attention linear projection and softmax](../../wiki-assets/jay-alammar-the-illustrated-transformer/full-two-layer-transformer.png)

- Decoding is autoregressive. Encoder outputs supply keys and values to every decoder's cross-attention; masked decoder self-attention blocks future output positions, and each emitted token becomes input to the next step until the end symbol.

![Animation of decoder time steps using the encoded input through cross-attention](../../wiki-assets/jay-alammar-the-illustrated-transformer/encoder-decoder-cross-attention.gif)

![Animation of autoregressive decoding with each previous output fed back as the next decoder input](../../wiki-assets/jay-alammar-the-illustrated-transformer/autoregressive-decoding-sequence.gif)

- A final linear layer maps the decoder vector to one logit per output-vocabulary item; softmax turns these into probabilities. Greedy decoding picks the highest-probability item, while beam search keeps several partial hypotheses.

![Decoder output projected to vocabulary logits normalized by softmax and selected by argmax](../../wiki-assets/jay-alammar-the-illustrated-transformer/final-linear-softmax-output.png)

- During supervised training, each expected output token is represented as a target distribution over the vocabulary. Backpropagation changes model weights so the predicted distributions move toward those targets at every output position.

![Six-word toy output vocabulary mapping words and end-of-sequence to numeric indexes](../../wiki-assets/jay-alammar-the-illustrated-transformer/toy-output-vocabulary.png)

![One-hot vector marking the vocabulary index for the word am](../../wiki-assets/jay-alammar-the-illustrated-transformer/one-hot-target-word.png)

![Untrained model probability distribution compared with the one-hot target for thanks](../../wiki-assets/jay-alammar-the-illustrated-transformer/untrained-versus-target-distribution.png)

![Five target one-hot distributions for I am a student followed by end-of-sequence](../../wiki-assets/jay-alammar-the-illustrated-transformer/sequence-target-distributions.png)

![Trained model distributions assigning high probability to I am a student and end-of-sequence](../../wiki-assets/jay-alammar-the-illustrated-transformer/trained-sequence-distributions.png)

## Key Quotes
> “self attention allows it to look at other positions in the input sequence” - on contextualizing each token.

> “we concat the matrices then multiply them by an additional weights matrix” - on merging attention heads.

## Connections
- [[JayAlammar]] - author and visual explainer of the architecture.
- [[TransformerArchitecture]] - the encoder-decoder model decomposed by the article.
- [[AttentionMechanism]] - the query-key-value computation at the center of each stack.
- [[PositionalEncoding]] - the added signal that makes token order available to attention.
- [[Embeddings]] - vector representations supplied to the first encoder and decoder layers.
- [[NeuralNetworkTraining]] - backpropagation adjusts projections, sublayers, and output distributions toward labeled targets.
- [[NaturalLanguageProcessing]] - machine translation is the running application.

## Contradictions
- The article explains the original 2017 encoder-decoder Transformer with six layers, eight heads, 512-wide states, and sinusoidal positions. Those figures do not describe all later encoder-only, decoder-only, or modified-attention architectures.
- Its early positional-encoding heatmap came from Tensor2Tensor's concatenated implementation; the 2020 update correctly distinguishes the paper's interleaved sine and cosine dimensions.
- The statement that two probability distributions can “simply” be subtracted is a pedagogical shortcut, not a loss-function specification; the linked discussion points to cross-entropy and KL divergence.
- Attention-line visualizations show model weights for one input and layer. They do not establish that a head has a stable linguistic role or that its weights fully explain the model's decision.
