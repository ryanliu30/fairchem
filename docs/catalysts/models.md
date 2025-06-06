# Pretrained models

**2025 recommendation:** We now suggest using the [UMA model](../core/uma), trained on all of the FAIR chemistry datasets before using one of the checkpoints below. The UMA model has a number of nice features over the previous checkpoints
1. It is state-of-the-art in out-of-domain prediction accuracy
2. It predicts total energies of a system, which are helpful for predicting properties beyond adsorption energies, and removes some ambiguity when your catalyst surface may reconstruct. 
3. The UMA small model is an energy conserving and smooth checkpoint, so should work much better for vibrational calculations, molecular dynamics, etc. 
4. The UMA model is most likely to be updated in the future.

## Legacy FAIRChemV1 Models Trained on Open Catalyst 2020 (OC20)

This page summarizes all the pretrained models released as part of the [Open Catalyst Project](https://opencatalystproject.org/), and are only available if you install fairchem<=2.0


* All configurations for these models are available in the [`configs/`](https://github.com/facebookresearch/fairchem/tree/main/configs) directory.
* All of these models are trained on various splits of the OC20 S2EF / IS2RE datasets. For details, see [https://arxiv.org/abs/2010.09990](https://arxiv.org/abs/2010.09990) and https://github.com/facebookresearch/fairchem/blob/main/DATASET.md.
* All OC20 models are trained on adsorption energies, i.e. the DFT total energies minus the clean surface and gas phase adsorbate energies. For details on how to train models on OC20 total energies, please read the [referencing section here](https://fair-chem.github.io/core/datasets/oc20.html).

### S2EF models: optimized for EFwT

| Model Name                          | Model	              | Split  |Download	|val ID force MAE (eV / Å)	|val ID EFwT	|
|-------------------------------------|---------------------|--------|---	|---	|---	|
| CGCNN-S2EF-OC20-200k               | CGCNN               | 200k	  |[checkpoint](https://dl.fbaipublicfiles.com/opencatalystproject/models/2020_11/s2ef/cgcnn_200k.pt) \| [config](https://github.com/facebookresearch/fairchem/blob/main/configs/oc20/s2ef/200k/cgcnn/cgcnn.yml)	|0.08	|0%	|
| CGCNN-S2EF-OC20-2M                 | CGCNN               | 2M	    |[checkpoint](https://dl.fbaipublicfiles.com/opencatalystproject/models/2020_11/s2ef/cgcnn_2M.pt) \| [config](https://github.com/facebookresearch/fairchem/blob/main/configs/oc20/s2ef/2M/cgcnn/cgcnn.yml)	|0.0673	|0.01%	|
| CGCNN-S2EF-OC20-20M                | CGCNN               | 20M	   |[checkpoint](https://dl.fbaipublicfiles.com/opencatalystproject/models/2020_11/s2ef/cgcnn_20M.pt) \| [config](https://github.com/facebookresearch/fairchem/blob/main/configs/oc20/s2ef/20M/cgcnn/cgcnn.yml)	|0.065	|0%	|
| CGCNN-S2EF-OC20-All                | CGCNN               | All	   |[checkpoint](https://dl.fbaipublicfiles.com/opencatalystproject/models/2020_11/s2ef/cgcnn_all.pt) \| [config](https://github.com/facebookresearch/fairchem/blob/main/configs/oc20/s2ef/all/cgcnn/cgcnn.yml)	|0.0684	|0.01%	|
| DimeNet-S2EF-OC20-200k             | DimeNet             | 200k	  |[checkpoint](https://dl.fbaipublicfiles.com/opencatalystproject/models/2020_11/s2ef/dimenet_200k.pt)	|0.0693	|0.01%	|
| DimeNet-S2EF-OC20-2M               | DimeNet             | 2M	    |[checkpoint](https://dl.fbaipublicfiles.com/opencatalystproject/models/2020_11/s2ef/dimenet_2M.pt)	|0.0576	|0.02%	|
| SchNet-S2EF-OC20-200k              | SchNet              | 200k	  |[checkpoint](https://dl.fbaipublicfiles.com/opencatalystproject/models/2020_11/s2ef/schnet_200k.pt) \| [config](https://github.com/facebookresearch/fairchem/blob/main/configs/oc20/s2ef/200k/schnet/schnet.yml)	|0.0743	|0%	|
| SchNet-S2EF-OC20-2M                | SchNet              | 2M	    |[checkpoint](https://dl.fbaipublicfiles.com/opencatalystproject/models/2020_11/s2ef/schnet_2M.pt) \| [config](https://github.com/facebookresearch/fairchem/blob/main/configs/oc20/s2ef/2M/schnet/schnet.yml)	|0.0737	|0%	|
| SchNet-S2EF-OC20-20M               | SchNet              | 20M	   |[checkpoint](https://dl.fbaipublicfiles.com/opencatalystproject/models/2020_11/s2ef/schnet_20M.pt) \| [config](https://github.com/facebookresearch/fairchem/blob/main/configs/oc20/s2ef/20M/schnet/schnet.yml)	|0.0568	|0.03%	|
| SchNet-S2EF-OC20-All               | SchNet              | All	   |[checkpoint](https://dl.fbaipublicfiles.com/opencatalystproject/models/2020_11/s2ef/schnet_all_large.pt) \| [config](https://github.com/facebookresearch/fairchem/blob/main/configs/oc20/s2ef/all/schnet/schnet.yml)	|0.0494	|0.12%	|
| DimeNet++-S2EF-OC20-200k           | DimeNet++           | 200k   |[checkpoint](https://dl.fbaipublicfiles.com/opencatalystproject/models/2021_02/s2ef/dimenetpp_200k.pt) \| [config](https://github.com/facebookresearch/fairchem/blob/main/configs/oc20/s2ef/200k/dimenet_plus_plus/dpp.yml)	|0.0741	|0%	|
| DimeNet++-S2EF-OC20-2M             | DimeNet++           | 2M     |[checkpoint](https://dl.fbaipublicfiles.com/opencatalystproject/models/2021_02/s2ef/dimenetpp_2M.pt) \| [config](https://github.com/facebookresearch/fairchem/blob/main/configs/oc20/s2ef/2M/dimenet_plus_plus/dpp.yml)	|0.0595	|0.01%	|
| DimeNet++-S2EF-OC20-20M            | DimeNet++           | 20M    |[checkpoint](https://dl.fbaipublicfiles.com/opencatalystproject/models/2021_02/s2ef/dimenetpp_20M.pt) \| [config](https://github.com/facebookresearch/fairchem/blob/main/configs/oc20/s2ef/20M/dimenet_plus_plus/dpp.yml)	|0.0511	|0.06%	|
| DimeNet++-S2EF-OC20-All            | DimeNet++           | All    |[checkpoint](https://dl.fbaipublicfiles.com/opencatalystproject/models/2021_02/s2ef/dimenetpp_all.pt) \| [config](https://github.com/facebookresearch/fairchem/blob/main/configs/oc20/s2ef/all/dimenet_plus_plus/dpp.yml)	|0.0444	|0.12%	|
| SpinConv-S2EF-OC20-2M              | SpinConv            | 2M     |[checkpoint](https://dl.fbaipublicfiles.com/opencatalystproject/models/2021_12/s2ef/spinconv_force_centric_2M.pt) \| [config](https://github.com/facebookresearch/fairchem/blob/main/configs/oc20/s2ef/2M/spinconv/spinconv_force.yml)	|0.0329	|0.18%	|
| SpinConv-S2EF-OC20-All             | SpinConv            | All    |[checkpoint](https://dl.fbaipublicfiles.com/opencatalystproject/models/2021_08/s2ef/spinconv_force_centric_all.pt) \| [config](https://github.com/facebookresearch/fairchem/blob/main/configs/oc20/s2ef/all/spinconv/spinconv_force.yml)	|0.0267	|1.02%	|
| GemNet-dT-S2EF-OC20-2M             | GemNet-dT           | 2M     |[checkpoint](https://dl.fbaipublicfiles.com/opencatalystproject/models/2021_12/s2ef/gemnet_t_direct_h512_2M.pt) \| [config](https://github.com/facebookresearch/fairchem/blob/main/configs/oc20/s2ef/2M/gemnet/gemnet-dT.yml)	|0.0257	|1.10%	|
| GemNet-dT-S2EF-OC20-All            | GemNet-dT           | All    |[checkpoint](https://dl.fbaipublicfiles.com/opencatalystproject/models/2021_08/s2ef/gemnet_t_direct_h512_all.pt) \| [config](https://github.com/facebookresearch/fairchem/blob/main/configs/oc20/s2ef/all/gemnet/gemnet-dT.yml)	|0.0211	|2.21%	|
| PaiNN-S2EF-OC20-All                | PaiNN               | All    |[checkpoint](https://dl.fbaipublicfiles.com/opencatalystproject/models/2022_05/s2ef/painn_h512_s2ef_all.pt) \| [config](https://github.com/facebookresearch/fairchem/blob/main/configs/oc20/s2ef/all/painn/painn_h512.yml) \| [scale file](https://github.com/facebookresearch/fairchem/blob/main/configs/oc20/s2ef/all/painn/painn_nb6_scaling_factors.pt)     |0.0294 |0.91%   |
| GemNet-OC-S2EF-OC20-2M             | GemNet-OC           | 2M     |[checkpoint](https://dl.fbaipublicfiles.com/opencatalystproject/models/2022_07/s2ef/gemnet_oc_base_s2ef_2M.pt) \| [config](https://github.com/facebookresearch/fairchem/blob/main/configs/oc20/s2ef/2M/gemnet/gemnet-oc.yml) \| [scale file](https://github.com/facebookresearch/fairchem/blob/481f3a5a92dc787384ddae9fe3f50f5d932712fd/configs/oc20/s2ef/all/gemnet/scaling_factors/gemnet-oc.pt)  |0.0225 |2.12%  |
| GemNet-OC-S2EF-OC20-All            | GemNet-OC           | All    |[checkpoint](https://dl.fbaipublicfiles.com/opencatalystproject/models/2022_07/s2ef/gemnet_oc_base_s2ef_all.pt) \| [config](https://github.com/facebookresearch/fairchem/blob/main/configs/oc20/s2ef/all/gemnet/gemnet-oc.yml) \| [scale file](https://github.com/facebookresearch/fairchem/blob/481f3a5a92dc787384ddae9fe3f50f5d932712fd/configs/oc20/s2ef/all/gemnet/scaling_factors/gemnet-oc.pt) |0.0179 |4.56%  |
| GemNet-OC-S2EF-OC20-All+MD         | GemNet-OC           | All+MD |[checkpoint](https://dl.fbaipublicfiles.com/opencatalystproject/models/2023_03/s2ef/gemnet_oc_base_s2ef_all_md.pt) \| [config](https://github.com/facebookresearch/fairchem/blob/main/configs/oc20/s2ef/all/gemnet/gemnet-oc.yml) \| [scale file](https://github.com/facebookresearch/fairchem/blob/481f3a5a92dc787384ddae9fe3f50f5d932712fd/configs/oc20/s2ef/all/gemnet/scaling_factors/gemnet-oc.pt) |0.0173 |4.72%  |
| GemNet-OC-Large-S2EF-OC20-All+MD   | GemNet-OC-Large     | All+MD |[checkpoint](https://dl.fbaipublicfiles.com/opencatalystproject/models/2022_07/s2ef/gemnet_oc_large_s2ef_all_md.pt) \| [config](https://github.com/facebookresearch/fairchem/blob/main/configs/oc20/s2ef/all/gemnet/gemnet-oc-large.yml) \| [scale file](https://github.com/facebookresearch/fairchem/blob/481f3a5a92dc787384ddae9fe3f50f5d932712fd/configs/oc20/s2ef/all/gemnet/scaling_factors/gemnet-oc-large.pt) |0.0164 |5.34%  |
| SCN-S2EF-OC20-2M                   | SCN                 | 2M     |[checkpoint](https://dl.fbaipublicfiles.com/opencatalystproject/models/2023_03/s2ef/scn_t1_b1_s2ef_2M.pt) \| [config](https://github.com/facebookresearch/fairchem/blob/main/configs/oc20/s2ef/2M/scn/scn-t1-b1.yml) |0.0216 |1.68%  |
| SCN-t4-b2-S2EF-OC20-2M             | SCN-t4-b2           | 2M     |[checkpoint](https://dl.fbaipublicfiles.com/opencatalystproject/models/2023_03/s2ef/scn_t4_b2_s2ef_2M.pt) \| [config](https://github.com/facebookresearch/fairchem/blob/main/configs/oc20/s2ef/2M/scn/scn-t4-b2.yml) |0.0193 |2.68%  |
| SCN-S2EF-OC20-All+MD               | SCN                 | All+MD |[checkpoint](https://dl.fbaipublicfiles.com/opencatalystproject/models/2023_03/s2ef/scn_all_md_s2ef.pt) \| [config](https://github.com/facebookresearch/fairchem/blob/main/configs/oc20/s2ef/all/scn/scn-all-md.yml) |0.0160 |5.08%  |
| eSCN-L4-M2-Lay12-S2EF-OC20-2M      | eSCN-L4-M2-Lay12    | 2M     |[checkpoint](https://dl.fbaipublicfiles.com/opencatalystproject/models/2023_03/s2ef/escn_l4_m2_lay12_2M_s2ef.pt) \| [config](https://github.com/facebookresearch/fairchem/blob/main/configs/oc20/s2ef/2M/escn/eSCN-L4-M2-Lay12.yml) |0.0191 |2.55%  |
| eSCN-L6-M2-Lay12-S2EF-OC20-2M      | eSCN-L6-M2-Lay12    | 2M     |[checkpoint](https://dl.fbaipublicfiles.com/opencatalystproject/models/2023_03/s2ef/escn_l6_m2_lay12_2M_s2ef.pt) \| [config](https://github.com/facebookresearch/fairchem/blob/main/configs/oc20/s2ef/2M/escn/eSCN-L6-M2-Lay12.yml) \| [exported](https://dl.fbaipublicfiles.com/opencatalystproject/models/2023_03/s2ef/escn_l6_m2_lay12_2M_s2ef_export_cuda_9182024.pt2) |0.0186 |2.66%  |
| eSCN-L6-M2-Lay12-S2EF-OC20-All+MD  | eSCN-L6-M2-Lay12    | All+MD |[checkpoint](https://dl.fbaipublicfiles.com/opencatalystproject/models/2023_03/s2ef/escn_l6_m2_lay12_all_md_s2ef.pt) \| [config](https://github.com/facebookresearch/fairchem/blob/main/configs/oc20/s2ef/all/escn/eSCN-L6-M2-Lay12-All-MD.yml) |0.0161 |4.28%  |
| eSCN-L6-M3-Lay20-S2EF-OC20-All+MD  | eSCN-L6-M3-Lay20    | All+MD |[checkpoint](https://dl.fbaipublicfiles.com/opencatalystproject/models/2023_03/s2ef/escn_l6_m3_lay20_all_md_s2ef.pt) \| [config](https://github.com/facebookresearch/fairchem/blob/main/configs/oc20/s2ef/all/escn/eSCN-L6-M3-Lay20-All-MD.yml) |0.0139 |6.64%  |
| EquiformerV2-83M-S2EF-OC20-2M      | EquiformerV2 (83M)  | 2M     |[checkpoint](https://dl.fbaipublicfiles.com/opencatalystproject/models/2023_06/oc20/s2ef/eq2_83M_2M.pt) \| [config](https://github.com/facebookresearch/fairchem/blob/main/configs/oc20/s2ef/2M/equiformer_v2/equiformer_v2_N@12_L@6_M@2.yml) |0.0167 |4.26%  |
| EquiformerV2-31M-S2EF-OC20-All+MD  | EquiformerV2 (31M)  | All+MD |[checkpoint](https://dl.fbaipublicfiles.com/opencatalystproject/models/2023_06/oc20/s2ef/eq2_31M_ec4_allmd.pt) \| [config](https://github.com/facebookresearch/fairchem/blob/main/configs/oc20/s2ef/all/equiformer_v2/equiformer_v2_N@8_L@4_M@2_31M.yml) |0.0142  |6.20%  |
| EquiformerV2-153M-S2EF-OC20-All+MD | EquiformerV2 (153M) | All+MD |[checkpoint](https://dl.fbaipublicfiles.com/opencatalystproject/models/2023_06/oc20/s2ef/eq2_153M_ec4_allmd.pt) \| [config](https://github.com/facebookresearch/fairchem/blob/main/configs/oc20/s2ef/all/equiformer_v2/equiformer_v2_N@20_L@6_M@3_153M.yml)   |0.0126     |8.90%  |

### S2EF models: optimized for force only

| Model Name                           |Model	|Split	|Download	|val ID force MAE	|
|--------------------------------------|---	|---	|---	|---	|
| SchNet-S2EF-force-only-OC20-All            |SchNet	|All	|[checkpoint](https://dl.fbaipublicfiles.com/opencatalystproject/models/2020_11/s2ef/schnet_all_forceonly.pt)	|0.0443	|
| DimeNet++-force-only-OC20-All              | DimeNet++	                |All	|[checkpoint](https://dl.fbaipublicfiles.com/opencatalystproject/models/2020_11/s2ef/dimenetpp_all_forceonly.pt) \| [config](https://github.com/facebookresearch/fairchem/blob/main/configs/oc20/s2ef/all/dimenet_plus_plus/dpp_forceonly.yml)	|0.0334	|
| DimeNet++-Large-S2EF-force-only-OC20-All   | DimeNet++-Large	          |All	|[checkpoint](https://dl.fbaipublicfiles.com/opencatalystproject/models/2021_02/s2ef/dimenetpp_large_all_forceonly.pt) \| [config](https://github.com/facebookresearch/fairchem/blob/main/configs/oc20/s2ef/all/dimenet_plus_plus/dpp10.7M_forceonly.yml)	|0.02825	|
| DimeNet++-S2EF-force-only-OC20-20M+Rattled | DimeNet++	                |20M+Rattled    |[checkpoint](https://dl.fbaipublicfiles.com/opencatalystproject/models/2021_02/s2ef/dimenetpp_20M_rattled_forceonly.pt)	|0.0614	|
| DimeNet++-S2EF-force-only-OC20-20M+MD      | DimeNet++	                |20M+MD         |[checkpoint](https://dl.fbaipublicfiles.com/opencatalystproject/models/2021_02/s2ef/dimenetpp_20M_md_forceonly.pt)	|0.0594	|

### IS2RE models

| Model Name                | Model	     | Split	 |Download	|val ID energy MAE	|
|---------------------------|------------|--------|---	|---	|
| CGCNN-IS2RE-OC20-10k      | CGCNN      | 10k    |[checkpoint](https://dl.fbaipublicfiles.com/opencatalystproject/models/2021_02/is2re/cgcnn_10k.pt) \| [config](https://github.com/facebookresearch/fairchem/blob/main/configs/oc20/is2re/10k/cgcnn/cgcnn.yml)	|0.9881	|
| CGCNN-IS2RE-OC20-100k     | CGCNN      | 100k   |[checkpoint](https://dl.fbaipublicfiles.com/opencatalystproject/models/2021_02/is2re/cgcnn_100k.pt) \| [config](https://github.com/facebookresearch/fairchem/blob/main/configs/oc20/is2re/100k/cgcnn/cgcnn.yml)	|0.682	|
| CGCNN-IS2RE-OC20-All      | CGCNN      | All    |[checkpoint](https://dl.fbaipublicfiles.com/opencatalystproject/models/2021_02/is2re/cgcnn_all.pt) \| [config](https://github.com/facebookresearch/fairchem/blob/main/configs/oc20/is2re/all/cgcnn/cgcnn.yml)	|0.6199	|
| DimeNet-IS2RE-OC20-10k    | DimeNet    | 10k    |[checkpoint](https://dl.fbaipublicfiles.com/opencatalystproject/models/2020_11/is2re/dimenet_10k.pt)	|1.0117	|
| DimeNet-IS2RE-OC20-100k   | DimeNet    | 100k   |[checkpoint](https://dl.fbaipublicfiles.com/opencatalystproject/models/2020_11/is2re/dimenet_100k.pt)	|0.6658	|
| DimeNet-IS2RE-OC20-all    | DimeNet    | All    |[checkpoint](https://dl.fbaipublicfiles.com/opencatalystproject/models/2020_11/is2re/dimenet_all.pt)	|0.5999	|
| SchNet-IS2RE-OC20-10k     | SchNet     | 10k    |[checkpoint](https://dl.fbaipublicfiles.com/opencatalystproject/models/2021_02/is2re/schnet_10k.pt) \| [config](https://github.com/facebookresearch/fairchem/blob/main/configs/oc20/is2re/10k/schnet/schnet.yml)	|1.059	|
| SchNet-IS2RE-OC20-100k    | SchNet     | 100k   |[checkpoint](https://dl.fbaipublicfiles.com/opencatalystproject/models/2021_02/is2re/schnet_100k.pt) \| [config](https://github.com/facebookresearch/fairchem/blob/main/configs/oc20/is2re/100k/schnet/schnet.yml)	|0.7137	|
| SchNet-IS2RE-OC20-All     | SchNet     | All    |[checkpoint](https://dl.fbaipublicfiles.com/opencatalystproject/models/2021_02/is2re/schnet_all.pt) \| [config](https://github.com/facebookresearch/fairchem/blob/main/configs/oc20/is2re/all/schnet/schnet.yml)	|0.6458	|
| DimeNet++-IS2RE-OC20-10k  | DimeNet++	 | 10k	   |[checkpoint](https://dl.fbaipublicfiles.com/opencatalystproject/models/2021_02/is2re/dimenetpp_10k.pt) \| [config](https://github.com/facebookresearch/fairchem/blob/main/configs/oc20/is2re/10k/dimenet_plus_plus/dpp.yml)	|0.8837	|
| DimeNet++-IS2RE-OC20-100k | DimeNet++	 | 100k   |[checkpoint](https://dl.fbaipublicfiles.com/opencatalystproject/models/2021_02/is2re/dimenetpp_100k.pt) \| [config](https://github.com/facebookresearch/fairchem/blob/main/configs/oc20/is2re/100k/dimenet_plus_plus/dpp.yml)	|0.6388	|
| DimeNet++-IS2RE-OC20-All  | DimeNet++	 | All	   |[checkpoint](https://dl.fbaipublicfiles.com/opencatalystproject/models/2021_02/is2re/dimenetpp_all.pt) \| [config](https://github.com/facebookresearch/fairchem/blob/main/configs/oc20/is2re/all/dimenet_plus_plus/dpp.yml)	|0.5639	|
| PaiNN-IS2RE-OC20-All      | PaiNN      | All    |[checkpoint](https://dl.fbaipublicfiles.com/opencatalystproject/models/2022_05/is2re/painn_h1024_bs4x8_is2re_all.pt) \| [config](https://github.com/facebookresearch/fairchem/blob/main/configs/oc20/is2re/all/painn/painn_h1024_bs8x4.yml) \| [scale file](https://github.com/facebookresearch/fairchem/blob/main/configs/oc20/s2ef/all/painn/painn_nb6_scaling_factors.pt)     |0.5728 |

The Open Catalyst 2020 (OC20) dataset is licensed under a [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/legalcode).

Please consider citing the following paper in any research manuscript using the
OC20 dataset or pretrained models, as well as the original paper for each model:

```bibtex
@article{ocp_dataset,
    author = {Chanussot*, Lowik and Das*, Abhishek and Goyal*, Siddharth and Lavril*, Thibaut and Shuaibi*, Muhammed and Riviere, Morgane and Tran, Kevin and Heras-Domingo, Javier and Ho, Caleb and Hu, Weihua and Palizhati, Aini and Sriram, Anuroop and Wood, Brandon and Yoon, Junwoong and Parikh, Devi and Zitnick, C. Lawrence and Ulissi, Zachary},
    title = {Open Catalyst 2020 (OC20) Dataset and Community Challenges},
    journal = {ACS Catalysis},
    year = {2021},
    doi = {10.1021/acscatal.0c04525},
}
```

## Open Catalyst 2022 (OC22)

* All configurations for these models are available in the [`configs/oc22`](https://github.com/facebookresearch/fairchem/tree/main/configs/oc22) directory.
* All of these models are trained on various splits of the OC22 S2EF / IS2RE datasets. For details, see [https://arxiv.org/abs/2206.08917](https://arxiv.org/abs/2206.08917) and https://github.com/facebookresearch/fairchem/blob/main/DATASET.md.
* All OC22 models released here are trained on DFT total energies, in contrast to the OC20 models listed above, which are trained on adsorption energies.


### S2EF-Total models

| Model Name                        |Model	|Training	|Download	|val ID force MAE	|val ID energy MAE	|
|-----------------------------------|---	|---	|---	|---	|---	|
| GemNet-dT-S2EFS-OC22              |GemNet-dT | OC22	|[checkpoint](https://dl.fbaipublicfiles.com/opencatalystproject/models/2022_09/oc22/s2ef/gndt_oc22_all_s2ef.pt) \| [config](https://github.com/facebookresearch/fairchem/blob/main/configs/oc22/s2ef/gemnet-dt/gemnet-dT.yml)	|0.032	|1.127	|
| GemNet-OC-S2EFS-OC22              | GemNet-OC                                                                                                                                                | OC22	|[checkpoint](https://dl.fbaipublicfiles.com/opencatalystproject/models/2022_09/oc22/s2ef/gnoc_oc22_all_s2ef.pt) \| [config](https://github.com/facebookresearch/fairchem/blob/main/configs/oc22/s2ef/gemnet-oc/gemnet_oc.yml)	|0.030	|0.563	|
| GemNet-OC-S2EFS-OC20+OC22         | GemNet-OC                                                                                                                                                | OC20+OC22	|[checkpoint](https://dl.fbaipublicfiles.com/opencatalystproject/models/2022_09/oc22/s2ef/gnoc_oc22_oc20_all_s2ef.pt) \| [config](https://github.com/facebookresearch/fairchem/blob/main/configs/oc22/s2ef/gemnet-oc/gemnet_oc_oc20_oc22.yml)	|0.027	|0.483	|
| GemNet-OC-S2EFS-nsn-OC20+OC22     | GemNet-OC <br><sub><sup>(trained with `enforce_max_neighbors_strictly=False`, [#467](https://github.com/facebookresearch/fairchem/pull/467))</sup></sub> | OC20+OC22	|[checkpoint](https://dl.fbaipublicfiles.com/opencatalystproject/models/2023_05/oc22/s2ef/gnoc_oc22_oc20_all_s2ef.pt) \| [config](https://github.com/facebookresearch/fairchem/blob/main/configs/oc22/s2ef/gemnet-oc/gemnet_oc_oc20_oc22_degen_edges.yml)	|0.027	|0.458	|
| GemNet-OC-S2EFS-OC20->OC22        | GemNet-OC                                                                                                                                                | OC20->OC22	|[checkpoint](https://dl.fbaipublicfiles.com/opencatalystproject/models/2022_09/oc22/s2ef/gnoc_finetune_all_s2ef.pt) \| [config](https://github.com/facebookresearch/fairchem/blob/main/configs/oc22/s2ef/gemnet-oc/gemnet_oc_finetune.yml)	|0.030	|0.417	|
| EquiformerV2-lE4-lF100-S2EFS-OC22 | EquiformerV2 ($\lambda_E$=4, $\lambda_F$=100)                                                                                                            | OC22  | [checkpoint](https://dl.fbaipublicfiles.com/opencatalystproject/models/2023_10/oc22/s2ef/eq2_121M_e4_f100_oc22_s2ef.pt) \| [config](https://github.com/facebookresearch/fairchem/blob/main/configs/oc22/s2ef/equiformer_v2/equiformer_v2_N@18_L@6_M@2_e4_f100_121M.yml) | 0.023 | 0.447

The Open Catalyst 2022 (OC22) dataset is licensed under a [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/legalcode).

Please consider citing the following paper in any research manuscript using the
OC22 dataset or pretrained models, as well as the original paper for each model:

```bibtex
@article{oc22_dataset,
    author = {Tran*, Richard and Lan*, Janice and Shuaibi*, Muhammed and Wood*, Brandon and Goyal*, Siddharth and Das, Abhishek and Heras-Domingo, Javier and Kolluru, Adeesh and Rizvi, Ammar and Shoghi, Nima and Sriram, Anuroop and Ulissi, Zachary and Zitnick, C. Lawrence},
    title = {The Open Catalyst 2022 (OC22) dataset and challenges for oxide electrocatalysts},
    journal = {ACS Catalysis},
    year={2023},
}
```
