pip install --upgrade pip
pip install --upgrade build
pip install --upgrade wheel
python3 -m build
pip install --force-reinstall ./dist/my_minipack-1.0.0-py3-none-any.whl