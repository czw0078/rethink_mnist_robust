import torch
import torch.nn as nn

class LeNet(nn.Module):
    def __init__(self):
        super(LeNet, self).__init__() # can be just super() in python 3
        self.conv1 = nn.Sequential(         
            nn.Conv2d(
                in_channels=1,  # Number of channels in the input image      
                out_channels=16, # Number of channels produced by the convolution           
                kernel_size=5,              
                stride=1,                   
                padding=2, # half of the kernel size 5 except middle 1       
            ),                              
            nn.ReLU(),                      
            nn.MaxPool2d(kernel_size=2),    
        )
        self.conv2 = nn.Sequential(         
            nn.Conv2d(16, 32, 5, 1, 2),     
            nn.ReLU(),                      
            nn.MaxPool2d(2),       
        )
        # fully connected layer, output 10 classes
        self.out = nn.Linear(32 * 7 * 7, 10)
        
    def forward(self, x):
        x = self.conv1(x)
        x = self.conv2(x)
        # flatten the output of conv2 to (batch_size, 32 * 7 * 7)
        x = x.view(x.size(0), -1)       
        output = self.out(x)
        return output    # do not return x for visualization

def trimmer(x, edge=0.3): # 0 to 0.5
    """
    >>> import torch
    >>> a = torch.Tensor([[0.7810, 0.2048, 0.2540],[0.4569, 0.3009, 0.1701]])
    >>> trimmer(a)
    tensor([[1.0000, 0.0000, 0.0000],
            [0.4569, 0.3009, 0.0000]])
    """

    low = edge
    high = 1 - edge

    select_high = x >= high
    select_low = x <= low

    x[select_high] = 1
    x[select_low] = 0

    return x

if __name__=="__main__":
    import doctest
    doctest.testmod()