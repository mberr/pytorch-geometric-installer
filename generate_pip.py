if __name__ == '__main__':
    try:
        import torch
    except ImportError:
        print("""
# Please install PyTorch first, cf. https://pytorch.org/get-started/locally/
pip install torch
        """)
        quit(-1)

    torch_version = torch.__version__
    cuda_version = torch.version.cuda
    cudnn_version = torch.backends.cudnn.version()
    gpu = torch.cuda.is_available()
    print(f"""\
# GPU available: {gpu}
# Versions
# Torch: {torch_version}
# CUDA : {cuda_version}
# CudNN: {cudnn_version}
""")

    TORCH = torch_version.split("+")[0]
    CUDA = "cu" + cuda_version.replace(".", "") if gpu else "cpu"

    print(f"""\
    
pip install torch-scatter -f https://data.pyg.org/whl/torch-{TORCH}+{CUDA}.html
pip install torch-sparse -f https://data.pyg.org/whl/torch-{TORCH}+{CUDA}.html
pip install torch-cluster -f https://data.pyg.org/whl/torch-{TORCH}+{CUDA}.html
pip install torch-spline-conv -f https://data.pyg.org/whl/torch-{TORCH}+{CUDA}.html
pip install torch-geometric
""")
