# PyTorch Geometric Install Helper

Generate pip install commands for installation of [PyTorch Geometric](https://github.com/rusty1s/pytorch_geometric) as described [here](https://github.com/rusty1s/pytorch_geometric#installation), e.g.

```console
$ python generate_pip.py
# GPU available: True
# Versions
# Torch: 1.10.0+cu113
# CUDA : 11.3
# CudNN: 8200

    
pip install torch-scatter -f https://data.pyg.org/whl/torch-1.10.0+cu113.html
pip install torch-sparse -f https://data.pyg.org/whl/torch-1.10.0+cu113.html
pip install torch-cluster -f https://data.pyg.org/whl/torch-1.10.0+cu113.html
pip install torch-spline-conv -f https://data.pyg.org/whl/torch-1.10.0+cu113.html
pip install torch-geometric
```

Requires [PyTorch](https://github.com/pytorch/pytorch) to be installed first.

*Note*: If the used PyTorch version was compiled for CUDA, but CUDA is not available for `torch`, it will install the cpu version of PyTorch Geometric.
