# Code Blocks Python00

### # 00.00.00 (conda version)

```
conda list
```

-----

### # 00.00.00 (python version)

```
pip list
```

-----

### # 00.00.01 (conda version)

```
conda list --export > requirements.txt
```

-----

### # 00.00.01 (python version)

```
pip freeze > requirements.txt
```

-----

### # 00.01.00

```
python exec.py "Hello" -> "OLLEh"
```

-----

### # 00.01.01

```
python exec.py "L337 5P3AK!" -> "!ka3p5 733l"
```

-----

### # 00.01.02

```
python exec.py "L337" "5P3AK!" -> "!ka3p5 733l"
```

-----

### # 00.01.03

```
python exec.py "L337" "" "5P3AK!" -> "!ka3p5   733l"
```

-----

### # 00.10.00

```
from loading import ft_progress
def test_X(X):
    for elem in ft_progress(X):
        ret += (elem + 3) % 5
        sleep(0.01)
    print()
    print(ret)
```