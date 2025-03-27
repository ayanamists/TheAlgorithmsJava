import shutil
import os.path as p
import subprocess

def taie_trans(original, target):
    current_dir = p.dirname(p.realpath(__file__))
    app_dir = p.join(p.dirname(p.dirname(current_dir)), 'app')
    subprocess.run(f"gradle taieTrans --args='{original} {target} 17'", shell=True, cwd=app_dir)

current_dir = p.dirname(p.realpath(__file__))
taie_trans(p.join(current_dir, 'target/Java-1.0-SNAPSHOT.jar'), p.join(current_dir, 'taie-trans/Java-1.0-SNAPSHOT-taie-trans.jar'))
