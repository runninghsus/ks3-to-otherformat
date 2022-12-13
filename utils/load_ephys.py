import numpy as np
import pandas as pd
import streamlit as st


class kilosort3_loader:

    def __init__(self, file_spike, file_cluster, file_group, file_info, fr_range, depth_range):

        self.spike_times = np.load(file_spike)
        self.clusters = np.load(file_cluster)
        self.cluster_labels = pd.read_csv(file_group, sep='\t')
        self.cluster_info = pd.read_csv(file_info, sep='\t')
        self.neuron_interest = []
        # some params
        self.fr_range = fr_range
        self.depth_range = depth_range

    def find_neurons(self):
        mua = 'Yes'
        if mua == 'Yes':
            for i, neuron in enumerate(np.unique(self.cluster_labels['cluster_id'])):
                if self.fr_range[0] <= self.cluster_info['fr'][i] < self.fr_range[1] \
                        and self.depth_range[0] <= self.cluster_info['depth'][i] < self.depth_range[1] \
                        and self.cluster_labels['group'][i] == 'good' \
                        or self.fr_range[0] <= self.cluster_info['fr'][i] < self.fr_range[1] \
                        and self.depth_range[0] <= self.cluster_info['depth'][i] < self.depth_range[1] \
                        and self.cluster_labels['group'][i] == 'mua':
                    self.neuron_interest.append(neuron)
        elif mua == 'No':
            for i, neuron in enumerate(np.unique(self.cluster_labels['cluster_id'])):
                if self.fr_range[0] <= self.cluster_info['fr'][i] < self.fr_range[1] \
                        and self.depth_range[0] <= self.cluster_info['depth'][i] < self.depth_range[1] \
                        and self.cluster_labels['group'][i] == 'good':
                    self.neuron_interest.append(neuron)

    def main(self):
        self.find_neurons()
        print('There are {} unique putative neurons ({} are included), '
              'spanning {} samples'.format(len(np.unique(self.clusters)),
                                           len(self.neuron_interest),
                                           len(self.spike_times)))
        return self.spike_times, self.clusters, self.neuron_interest


@st.cache
def get_neuron_spike(spike_times, clusters, good_clusters):
    sample_rate = 30000
    data_dict = {f'neuron {k}': [] for k in good_clusters}

    for i, neuron in enumerate(good_clusters):
        neuron_spike = spike_times[clusters == neuron]
        neuron_spike_s = np.hstack(neuron_spike / sample_rate)
        data_dict[f'neuron {neuron}'] = neuron_spike_s

    return data_dict