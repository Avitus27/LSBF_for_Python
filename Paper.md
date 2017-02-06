# A Proof of Concept for Locality Sensitive Bloom Filters

## Abstract
The goal of this paper is to provide an implimentation of Locality Sensitive Bloom Filters (LSBF) in Haskell, making use of Clash to generate HDL for running an FPGA example. Source code for verification of the implimentation is provided in the references.
This paper provides a base for further research which may include further optimizations and the implimentation of multi-dimentional sensitive hashing.

## Introduction



## References
[1] Distance-Sensitive Bloom Filters, A. Kirsch, M. Mitzenmacher 
[2] Practical and Optimal LSH for Angular Distance, A. Andoni, P. Indyk, T. Laarhoven, I. Razenshtyen
[3] GitHub - Avitus27: LSBF for Haskell, M. Galvin


## Personal Notes:

- Uses 1-dimension, a naive approach to the problem as implimentations of LSBF would likely want to make use of multiple feature, adding a dimension for each additional feature.



