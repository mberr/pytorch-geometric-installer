# PyTorch Geometric Install Helper

Generate pip install commands for installation of [PyTorch Geometric](https://github.com/rusty1s/pytorch_geometric) as described [here](https://github.com/rusty1s/pytorch_geometric#installation), e.g.

```console
$ python generate_pip.py
{'cuda': '10.2', 'cudnn': 7605, 'gpu': False, 'torch': '1.5.1'}

pip install --no-index torch-scatter -f https://pytorch-geometric.com/whl/torch-1.5.1+cpu.html
pip install --no-index torch-sparse -f https://pytorch-geometric.com/whl/torch-1.5.1+cpu.html
pip install --no-index torch-cluster -f https://pytorch-geometric.com/whl/torch-1.5.1+cpu.html
pip install --no-index torch-spline-conv -f https://pytorch-geometric.com/whl/torch-1.5.1+cpu.html
pip install torch-geometric
```

Requires [PyTorch](https://github.com/pytorch/pytorch) to be installed first.

*Note*: If the used PyTorch version was compiled for CUDA, but CUDA is not available for `torch`, it will install the cpu version of PyTorch Geometric.
