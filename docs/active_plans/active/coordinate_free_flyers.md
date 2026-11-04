# Plan: Coordinate-free flyer authoring

## Context

This repository builds single-page Letter flyers from nested YAML groups.

## Objectives

- Author rows and columns without page coordinates.
- Render local text, images, SVG artwork, and QR codes into one PDF.
- Use the redesigned StVC flyer as the first production source.

## Design philosophy

Use measured ReportLab flowables and a small YAML surface instead of a general layout solver.

## Scope

- Maintain the renderer, StVC source, bundled fonts, and authoring documentation.

## Non-goals

- Add absolute positions, automatic pagination, or a browser authoring interface.
