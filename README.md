# WebRobot
Scripts to realize ligand searching and docking task automatically in the course: [Introduction to Computational Structural Biology](https://catalog.upp.pitt.edu/preview_course_nopop.php?catoid=136&coid=735195).

## Task
See http://zincpharmer.csb.pitt.edu/pharmville/ for detailed description.

## Usage
* Under directory of WebRobot
```bash
mkdir inputData
mkdir outputData
```
* Under the parent directory of WebRobot
```bash
mkdir raw
```
Put ligand file (\*.sdf/\*.pdb) and receptor file (\*.pdb) under the *raw* directory.
* Run program
```bash
python run.py
```
* Extract final results

Please check *common_command*.
## Results
Used in the 2nd and 3rd task.
![alt tag](https://github.com/yifengtao/WebRobot/blob/master/rank.jpg)
