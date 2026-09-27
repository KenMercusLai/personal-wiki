---
title: "OpenCV"
type: entity
tags: [computer-vision, open-source, python]
sources:
  - detecting-cats-in-images-with-opencv-pyimagesearch
last_updated: 2026-09-27
knowledge_schema: synthesis-v1
---

## Overview
[[OpenCV]] is the computer-vision library used in the source to run pretrained cat-face detectors from Python.

## Current Profile
The source presents OpenCV as shipping trained classifiers as serialized XML files and exposing them through `cv2.CascadeClassifier` and `detectMultiScale`. Its repository included frontal-cat-face, extended frontal-cat-face, and LBP variants, making cat-face detection available without training an additional model.

## Key Characteristics
- Provides Python APIs for loading images, grayscale conversion, cascade inference, drawing boxes, display, and file output.
- Distributes pretrained object classifiers in Haar- and LBP-cascade directories.
- Supports multiscale detection in still images and, by applying the same operation frame by frame, video streams.
- Leaves important accuracy and performance choices to caller-supplied detection parameters.

## Evidence
- Included models: [[detecting-cats-in-images-with-opencv-pyimagesearch]] identifies frontal and extended cat-face XML cascades in OpenCV's Haar-cascade data.
- Runtime interface: [[detecting-cats-in-images-with-opencv-pyimagesearch]] uses `cv2.CascadeClassifier` and `detectMultiScale`, then draws returned rectangles.
- Supporting operations: [[detecting-cats-in-images-with-opencv-pyimagesearch]] uses grayscale conversion, display, and `cv2.imwrite` as parts of the workflow.
- Practical variability: [[detecting-cats-in-images-with-opencv-pyimagesearch]] records failures with different cascade files or parameter settings in its tutorial and discussion.

## Qualifications
This is a 2016 tutorial plus later comments, not current OpenCV documentation. Repository paths, bundled models, Python signatures, platform behavior, and compatibility may have changed, and the successful example images do not measure general detector accuracy.

## What Changed
- Created OpenCV's profile from the cat-face detection tutorial.

## Relationships
- [[HaarCascadeObjectDetection]] - OpenCV supplies the pretrained classifier and multiscale runtime used by the tutorial.
- [[HOGLinearSVMObjectDetection]] - the source presents this as an alternative detector family with different tuning and speed tradeoffs.
- [[JosephHowse]] - contributed the cat-face cascades described in the source.
- [[AdrianRosebrock]] - demonstrates OpenCV's cat detector in the source.
