import io
import numpy as np
import streamlit as st
import pandas as pd
from utils.ui import ks3_prompt
from utils.load_ephys import kilosort3_loader, get_neuron_spike
from utils.convert import df_to_csv

st.title('Kilosort3 to Other Formats')

col1, col2 = st.columns(2)
outname = col1.text_input('filename?', 'spiketimes')
selections = col2.multiselect('filetypes to save', ['csv', 'npy'], default='csv')
try:
    [file_spiketimes,
     file_clusters,
     file_group,
     file_info,
     fr_range, depth_range,
     ] = ks3_prompt()

    # load kilo3 files and filter by phy2 manual sorts
    spiketrain_loader = kilosort3_loader(file_spiketimes,
                                         file_clusters,
                                         file_group,
                                         file_info,
                                         fr_range, depth_range)
    spike_times, clusters, good_clusters = spiketrain_loader.main()

    # retrieve spike times and organize by neuron ID
    data_dict = get_neuron_spike(spike_times, clusters, good_clusters)

    # convert dictionary to dataframe
    st_by_neuron_df = pd.DataFrame(list(data_dict.values()),
                                   index=data_dict.keys())
    st_by_neuron_df = st_by_neuron_df.transpose()

    # convert to csv
    csv = df_to_csv(st_by_neuron_df)

    st.success(f'loaded {len(np.unique(clusters))} '
               f'unique putative neurons ({len(good_clusters)} are included) '
               f'spanning {len(spike_times)} samples')

    st.write('An example:')
    st.write(st_by_neuron_df.iloc[:50])

    if 'csv' in selections:
        st.download_button(
            label="Download CSV",
            data=csv,
            file_name=str.join('', (outname, '.csv')),
            mime='text/csv',
        )
    if 'npy' in selections:
        # Create an in-memory buffer
        with io.BytesIO() as buffer:
            # Write array to buffer
            np.save(buffer, data_dict)
            btn = st.download_button(
                label="Download NPY",
                data=buffer,  # Download buffer
                file_name=str.join('', (outname, '.npy'))
            )



except:
    pass
