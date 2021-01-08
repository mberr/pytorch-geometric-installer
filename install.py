from pprint import pprint

import torch

if __name__ == '__main__':
    torch_version = torch.__version__
    cuda_version = torch.version.cuda
    cudnn_version = torch.backends.cudnn.version()
    gpu = torch.cuda.is_available()
    pprint(dict(
        torch=torch_version,
        cuda=cuda_version,
        cudnn=cudnn_version,
        gpu=gpu,
    ))

    TORCH = torch_version
    CUDA = cuda_version.replace(".", "") if gpu else "cpu"

    print(f"""
pip install --no-index torch-scatter -f https://pytorch-geometric.com/whl/torch-{TORCH}+${CUDA}.html
pip install --no-index torch-sparse -f https://pytorch-geometric.com/whl/torch-{TORCH}+${CUDA}.html
pip install --no-index torch-cluster -f https://pytorch-geometric.com/whl/torch-{TORCH}+${CUDA}.html
pip install --no-index torch-spline-conv -f https://pytorch-geometric.com/whl/torch-{TORCH}+${CUDA}.html
pip install torch-geometric
    """)
