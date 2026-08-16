# Linear Algebra — Notes

Handwritten notes (`Linear_Algebra.pdf`) covering foundational linear algebra concepts, from vectors and vector spaces through matrix operations and solving linear systems.

## Contents

### Vectors & Vector Spaces
1. **R, R², R³, ... Rⁿ** — the real numbers and n-dimensional Euclidean spaces
2. **Vector norm (L2 norm / magnitude):** ‖v‖ = √(v₁² + v₂² + ... + vₙ²)
3. Unit circle coordinates: (x, y) = (cos θ, sin θ)
4. **Law of Sines** and **Law of Cosines** for triangles
5. **Euclidean distance** between two points: d = √((a₁-b₁)² + ... + (aₙ-bₙ)²)
6. **Scalar vs. Vector** — scalar as a single magnitude/quantity value; vector as an ordered array representing magnitude and direction
7. **Indexing in vectors** — standard notation (i = 1 to n), and the ambiguity between "element of a vector" vs. "vector in a collection" (nested vectors)
8. **Special vectors** — zero vector, unit vector, sparse vector
9. **Vector addition & subtraction** — element-wise, result is the same size
10. **Properties of vector addition** — commutative, associative, identity (zero vector), self-subtraction gives the zero vector
11. **Scalar multiplication** — scaling each component of a vector by a constant
12. **Dot product** — v·v = ‖v‖², a·b = a₁b₁ + a₂b₂ + ... + aₙbₙ = ‖a‖‖b‖cos θ; used as a measure of similarity/direction (same direction, perpendicular, opposite direction)
13. **Inner product** — generalizes the dot product to more abstract (including complex) vector spaces; involves conjugation for complex vectors, equivalent to the dot product for real vector spaces
14. **Cauchy-Schwarz inequality:** |⟨x, y⟩| ≤ ‖x‖‖y‖

### Linear Systems & Matrices
15. **Linear system** with m equations and n unknowns — general form
16. **Homogeneous vs. nonhomogeneous** systems (whether all constant terms bᵢ are zero)
17. **Matrix definition** — an m×n rectangular array of real numbers
18. **Matrix operations** — sum, difference, scalar multiplication, and matrix product (via dot product of rows and columns)
19. **Matrix representation of a linear system:** Ax = B
20. **Gaussian elimination** — systematic method to transform a system into row-echelon form; the augmented coefficient matrix [A|b]
21. **Row Echelon Form (REF)** — criteria: nonzero rows above zero rows, leading entries stepping right, zeros below leading entries (pivot/corner entry)
22. **Reduced Row Echelon Form (RREF)** — additional criteria: every leading entry is 1, and each leading 1 is the only nonzero entry in its column; includes a worked 3-equation, 3-unknown example solved via row reduction
23. **Solution cases for a linear system:**
    - No solution (inconsistent, e.g. 0 = 5)
    - Infinite solutions (no unique solution, e.g. more unknowns than equations)
    - Single (unique) solution

## Notes

- Written partly in Arabic/English mix (headers like "التاريخ" = Date, "الموضوع" = Subject).
- Includes a fully worked example of solving a 3×3 linear system via Gaussian elimination down to RREF.
