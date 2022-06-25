## Setup

```bash
0 @fake:[~/github/nephew]:$ virtualenv -p /usr/bin/python3 ~/virt3-nephew
Already using interpreter /usr/bin/python3
Using base prefix '/usr'
New python executable in /home/rmintz87/virt3-nephew/bin/python3
Also creating executable in /home/rmintz87/virt3-nephew/bin/python
Installing setuptools, pkg_resources, pip, wheel...done.
0 @fake:[~/github/nephew]:$ 

```

```bash
0 @fake:[~/github/nephew]:$ source ~/virt3-nephew/bin/activate
(virt3-nephew) 0 @fake:[~/github/nephew]:$ python --version 
Python 3.6.9
(virt3-nephew) 0 @fake:[~/github/nephew]:$ pip install chatterbot 
Collecting chatterbot
  Downloading ChatterBot-1.0.8-py2.py3-none-any.whl (63 kB)
     |████████████████████████████████| 63 kB 4.0 MB/s             
Collecting mathparse<0.2,>=0.1
  Downloading mathparse-0.1.2-py3-none-any.whl (7.2 kB)
Collecting pytz
  Using cached pytz-2022.1-py2.py3-none-any.whl (503 kB)
Collecting sqlalchemy<1.4,>=1.3
  Downloading SQLAlchemy-1.3.24-cp36-cp36m-manylinux2010_x86_64.whl (1.3 MB)
     |████████████████████████████████| 1.3 MB 15.7 MB/s            
Collecting python-dateutil<2.9,>=2.8
  Using cached python_dateutil-2.8.2-py2.py3-none-any.whl (247 kB)
Collecting six>=1.5
  Using cached six-1.16.0-py2.py3-none-any.whl (11 kB)
Installing collected packages: six, sqlalchemy, pytz, python-dateutil, mathparse, chatterbot
Successfully installed chatterbot-1.0.8 mathparse-0.1.2 python-dateutil-2.8.2 pytz-2022.1 six-1.16.0 sqlalchemy-1.3.24
(virt3-nephew) 0 @fake:[~/github/nephew]:$ 

```

```bash

(virt3-nephew) 0 @fake:[~/github/nephew]:$ ll
total 36
drwxrwxr-x  3 rmintz87 rmintz87  4096 Jun 24 20:28 ./
drwxrwxr-x 32 rmintz87 rmintz87  4096 Jun 24 20:19 ../
drwxrwxr-x  8 rmintz87 rmintz87  4096 Jun 24 20:28 .git/
-rw-rw-r--  1 rmintz87 rmintz87  1799 Jun 24 20:19 .gitignore
-rw-rw-r--  1 rmintz87 rmintz87  1652 Jun 24 20:28 README.md
-rw-rw-r--  1 rmintz87 rmintz87   383 Jun 24 20:28 README.md~
-rw-rw-r--  1 rmintz87 rmintz87 11627 Jun 24 20:19 stuff.py
(virt3-nephew) 0 @fake:[~/github/nephew]:$ chmod a+x stuff.py 
(virt3-nephew) 0 @fake:[~/github/nephew]:$ 

```

```bash
pip install spacy
```

```bash

python -m spacy download en
```

copy chatterbox required files to dir  
```bash
0 @fake:[~/github/chatterbot-corpus]:$ cp -rv chatterbot_corpus /home/rmintz87/
```
