# -*- coding: utf-8 -*-
# @Author       : William
# @Project      : TextGAN-william
# @FileName     : Oracle.py
# @Time         : Created at 2019-04-25
# @Blog         : http://zhiweil.ml/
# @Description  : 
# Copyrights (C) 2018. All Rights Reserved.

from models.generator import LSTMGenerator, TransformerGenerator


class Oracle(LSTMGenerator):

    def __init__(self, embedding_dim, hidden_dim, vocab_size, max_seq_len, padding_idx, gpu=False):
        super(Oracle, self).__init__(embedding_dim, hidden_dim, vocab_size, max_seq_len, padding_idx, gpu)
        self.name = 'oracle'

        # initialise oracle network with N(0,1)
        # otherwise variance of initialisation is very small => high NLL for loader sampled from the same model
        self.init_oracle()

class SAOracle(TransformerGenerator):

    def __init__(self, embedding_dim, hidden_dim, vocab_size, max_seq_len, padding_idx, num_heads=4, nlayers=4, dropout=0.5, gpu=False):
        super(SAOracle, self).__init__(embedding_dim, hidden_dim, vocab_size, max_seq_len, padding_idx, num_heads, nlayers, dropout, gpu)
        self.name = 'sa_oracle'

        self.init_oracle()
