# Eigenvalues-and-2D-Geometric-Transformations

This repository contains Python code that simulates **2D geometric transformations** using matrices and vectors.

## Implemented Transformations

### 1. Linear Transformations
The code applies transformations of the form:

F(X) = B X

to demonstrate:
- Rotation
- Scaling
- Reflection

Two different transformation matrices are computed to map an original shape to two transformed shapes.

### 2. Affine Transformations (with Translation)
To include translation, the code implements:

F(X) = V + B X

where:
- `B` is the transformation matrix (scaling + reflection)
- `V` is the translation vector

This is used to map an original shape to a translated and transformed shape.

## Output
- Visual plots of the original and transformed shapes
- Clear comparison between initial and final positions
