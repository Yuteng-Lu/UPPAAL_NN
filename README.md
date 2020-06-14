# UPPAAL_NN
We implement DeepAuto, utilizing UPPAAL model checker. The repository contains experiments, showing the practicability of DeepAuto. When we are interested in a specific DNN, we could use extract_weights.py to extract its weights. Based on extracted weights, we could construct formal model of the DNN following DeepAuto algorithm. DeepAuto workflow（shown in DeepAuto.png) describes the running process of our framework. 

From the technical perspective, we modify the xml file of normal FNN's UPPAAL model (shown as Fig.3 in submitted paper). We use import_weights.py based on the xml.etree.ElementTree module to achieve such modification.

When we model a DNN as a automaton based on DeepAuto algorithm, the data flow should be extracted first. And then we could use data flow to model the automaton, which actually represents the DNN's interior characteristics. Thus, even if we want to model a MNIST DNN, such difficult work could be done based on data flow. The model of a MNIST DNN is proposed in this repository and we will give the queries used to verify properties P1, P2 and P3. The modeling process is based on DeepAuto.

If you want to reoperate this experiment, you should install UPPAAL model checker. If you have any problems, please contact with luyuteng@pku.edu.cn. I will solve your problem.
