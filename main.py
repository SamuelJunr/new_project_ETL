import sys 
for path in sys.path:
    print(path)
    
sys.path.insert(0, "app\pipeline")