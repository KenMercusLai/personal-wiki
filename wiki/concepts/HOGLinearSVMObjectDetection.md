---
title: "HOG + Linear SVM Object Detection"
type: concept
tags: [computer-vision, object-detection, machine-learning]
sources:
  - detecting-cats-in-images-with-opencv-pyimagesearch
last_updated: 2026-09-27
knowledge_schema: synthesis-v1
---

## Definition
[[HOGLinearSVMObjectDetection]] is an object-detection framework that represents candidate windows with histograms of oriented gradients and classifies those features using a linear support vector machine.

## Current Synthesis
The source presents HOG plus a linear SVM mainly as a practical comparison point for Haar cascades. Its claimed advantage is lower false-positive behavior and parameters that are generally easier to tune; its cost is that real-time execution is harder to achieve. The article recommends it for custom object detectors but does not provide a direct experiment against the cat cascade.

## Key Claims
- HOG captures local edge-orientation structure for object classification.
- A linear SVM separates target-object windows from non-target windows using those features.
- The framework is presented as easier to tune than Haar-cascade `detectMultiScale` behavior.
- It is presented as producing substantially fewer false positives than Haar cascades.
- Real-time performance is described as more difficult to obtain.

## Evidence
- Comparative recommendation: [[detecting-cats-in-images-with-opencv-pyimagesearch]] says the author often applies HOG plus a linear SVM instead of Haar cascades.
- Accuracy rationale: [[detecting-cats-in-images-with-opencv-pyimagesearch]] attributes that preference to easier parameter tuning and a lower false-positive rate.
- Performance qualification: [[detecting-cats-in-images-with-opencv-pyimagesearch]] states that achieving real-time performance is the alternative's downside.
- Training scope: [[detecting-cats-in-images-with-opencv-pyimagesearch]] presents the framework as suitable for custom detectors for road signs, faces, cars, and other objects.

## Counterevidence & Qualifications
The source does not show HOG/SVM code, training data, measurements, or a controlled comparison with the cat cascade. Its accuracy and tuning claims are practitioner guidance, and actual behavior depends on features, sampling, hard-negative mining, window search, implementation, hardware, and target domain.

## What Changed
- Created the concept as the article's preferred alternative to Haar-cascade detection.

## Related Concepts
- [[HaarCascadeObjectDetection]] - baseline method against which the source states the tuning, false-positive, and speed tradeoffs.
- [[StatisticalError]] - lower false-positive behavior is the main claimed benefit, though it is not quantified here.
- [[SoftwareVerification]] - comparative detector claims require controlled datasets and repeatable evaluation.
