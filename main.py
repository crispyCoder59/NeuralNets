# -*- coding: utf-8 -*-
"""
Created on Sat Oct 21 23:40:03 2017

@author: Kevyn
"""
import run


def main():
    
    
    print("-------Standard Arguments-------")
    run.run_training(3.0)
    run.run_training(3.0)
    run.run_training(3.0)
    
    print("-------Learning Rate Test-------")
    
    """
    run.run_training(0.001)
    run.run_training(0.001)
    run.run_training(0.001)
    run.run_training(0.01)
    run.run_training(0.01)
    run.run_training(0.01)
    run.run_training(0.1)
    run.run_training(0.1)
    run.run_training(0.1)
    run.run_training(1.0)
    run.run_training(1.0)
    run.run_training(1.0)
    run.run_training(10.0)
    run.run_training(10.0)
    run.run_training(10.0)
    run.run_training(15.0)
    run.run_training(15.0)
    run.run_training(15.0)
    
    print("-------Epochs Test-------")
    run.run_training(3.0, 10)
    run.run_training(3.0, 20)
    run.run_training(3.0, 30)
    run.run_training(3.0, 40)
    run.run_training(3.0, 50)
    
    print("-------Mini Batch Size Test-------")
    run.run_training(3.0, 30, 1)
    run.run_training(3.0, 30, 5)
    run.run_training(3.0, 30, 10)
    run.run_training(3.0, 30, 15)
    run.run_training(3.0, 30, 20)
    run.run_training(3.0, 30, 25)
    run.run_training(3.0, 30, 100)
    
    print("-------One Hidden Layer Test-------")
    run.run_training(3.0, 30, 10, [4])
    run.run_training(3.0, 30, 10, [5])
    run.run_training(3.0, 30, 10, [6])
    run.run_training(3.0, 30, 10, [7])
    run.run_training(3.0, 30, 10, [8])
    run.run_training(3.0, 30, 10, [9])
    
    run.run_training(3.0, 30, 10, [10])
    run.run_training(3.0, 30, 10, [20])
    run.run_training(3.0, 30, 10, [30])
    run.run_training(3.0, 30, 10, [40])
    run.run_training(3.0, 30, 10, [50])
    run.run_training(3.0, 30, 10, [100])
    run.run_training(3.0, 30, 10, [300])
    
    print("-------Two Hidden Layer Test-------")
    run.run_training(3.0, 50, 10, [30, 30])
    run.run_training(3.0, 50, 10, [30, 30])
    run.run_training(3.0, 50, 10, [30, 30])
    
    run.run_training(3.0, 50, 10, [100, 30])
    run.run_training(3.0, 50, 10, [100, 30])
    run.run_training(3.0, 50, 10, [100, 30])
    
    run.run_training(3.0, 50, 10, [200, 30])
    run.run_training(3.0, 50, 10, [200, 30])
    run.run_training(3.0, 50, 10, [200, 30])
    
    run.run_training(3.0, 50, 10, [30, 100])
    run.run_training(3.0, 50, 10, [30, 100])
    run.run_training(3.0, 50, 10, [30, 100])
    
    run.run_training(3.0, 50, 10, [30, 200])
    run.run_training(3.0, 50, 10, [30, 200])
    run.run_training(3.0, 50, 10, [30, 200])
    
    """
    
    
if __name__ == "__main__":
    main()