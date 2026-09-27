---
title: "Adrian Rosebrock"
type: entity
tags: [computer-vision, education, pyimagesearch]
sources:
  - detecting-cats-in-images-with-opencv-pyimagesearch
last_updated: 2026-09-27
knowledge_schema: synthesis-v1
---

## Overview
[[AdrianRosebrock]] is the PyImageSearch author who wrote the source's practical tutorial on detecting cat faces with OpenCV.

## Current Profile
In this source, Rosebrock translates an existing pretrained classifier into a Python workflow, explains its parameters, tests it on visually varied examples, and answers implementation questions. He favors HOG plus a linear SVM for many custom-object tasks because of its lower false-positive rate and easier tuning, while recognizing the cascade's real-time advantage.

## Key Characteristics
- Teaches computer vision through executable Python and OpenCV examples.
- Connects API parameters to practical speed, recall, and false-positive tradeoffs.
- Uses multiple images to demonstrate behavior across occlusion, expression, composition, and subject count.
- Distinguishes an easy-to-run pretrained detector from a preferred but more involved alternative.

## Evidence
- Tutorial construction: [[detecting-cats-in-images-with-opencv-pyimagesearch]] walks from command-line arguments through image loading, inference, annotation, and display.
- Tradeoff explanation: [[detecting-cats-in-images-with-opencv-pyimagesearch]] explains the opposing consequences of large and small `scaleFactor` values and the role of `minNeighbors`.
- Comparative judgment: [[detecting-cats-in-images-with-opencv-pyimagesearch]] recommends HOG plus a linear SVM for lower false-positive rates while noting its real-time disadvantage.
- Reader support: [[detecting-cats-in-images-with-opencv-pyimagesearch]] includes answers about saving and cropping results, virtual environments, GUI failures, and detector tuning.

## Qualifications
The page reflects one tutorial and its comment thread. It does not establish Rosebrock's full biography, current views, or comparative performance claims beyond the source's examples and practitioner judgment.

## What Changed
- Created Rosebrock's profile from his OpenCV cat-detection tutorial.

## Relationships
- [[OpenCV]] - the library used throughout his tutorial.
- [[JosephHowse]] - trained the cat detector that Rosebrock demonstrates and credits.
- [[HaarCascadeObjectDetection]] - the tutorial's main detection method.
- [[HOGLinearSVMObjectDetection]] - Rosebrock's preferred alternative for easier tuning and fewer false positives.
