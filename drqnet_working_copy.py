from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

import functools
import numpy as np
import copy
import torch
import torch.nn as nn
import torch.optim as optim
from torch.nn import functional as F
from torch.autograd import Variable
from torch.nn.utils import clip_grad_norm_

import matplotlib.pyplot as plt

import gin.torch
import numpy as np



"""Inputs: tuple of (o_t^a, m_t-1^a', u_t-1^a, a
 a: player who's turn it is"""

#n-steps(DIAL) is update horizon(HLE)?

 # TODO: add gin configurable
class DRQNet(nn.Module):
    def __init__(self,
                 num_players = None,
                 observation_size = observation_size,
                 num_actions = None
                 rnn_size = 128,
                 comm_size = 2,
                 init_param_range = (-0.08 , 0.08),
                 target_update_period = 500,
                 update_period = 4,
                 epsilon_train = 0.02,
                 epsilon_eval = 0.001,
                 epsilon_decay = 1.0,
                 learning_rate = 0.0025,
                 momentum = 0.05):

 # TODO: replace comms with Bayesian belief update 