import streamlit as st


def ks3_prompt():

    uplodaed_files = st.file_uploader('please upload spike_times, '
                                      'spike_clusters,'
                                      'cluster_group, '
                                      'and cluster_info',
                                      accept_multiple_files=True)

    for f in uplodaed_files:
        if f.name == 'spike_times.npy':
            file_spiketimes = f
        elif f.name == 'spike_clusters.npy':
            file_clusters = f
        elif f.name == 'cluster_group.tsv':
            file_group = f
        elif f.name == 'cluster_info.tsv':
            file_info = f

    with st.sidebar:
        st.subheader('Parameters')
        min_fr = st.number_input('max firing rate',
                                 min_value=0.0, max_value=50.0,
                                 value=0.1)
        max_fr = st.number_input('max firing rate',
                                 min_value=0.2, max_value=100.0,
                                 value=30.0)
        fr_range = [min_fr, max_fr]
        min_depth = st.number_input('min depth',
                                    min_value=0, max_value=3840,
                                    value=2600)
        max_depth = st.number_input('max depth',
                                    min_value=0, max_value=3840,
                                    value=3840)
        depth_range = [min_depth, max_depth]

    return file_spiketimes, file_clusters, file_group, file_info, \
           fr_range, depth_range