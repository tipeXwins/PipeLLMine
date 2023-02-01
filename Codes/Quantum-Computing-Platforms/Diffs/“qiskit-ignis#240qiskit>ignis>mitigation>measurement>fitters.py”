46,47d45
<         A wrapper for the tensored fitter
< 
62a61,64
>         self._results = results
>         self._state_labels = state_labels
>         self._cal_matrix = None
>         self._circlabel = circlabel
67,70c69,70
<         self._tens_fitt = TensoredMeasFitter(results,
<                                              [qubit_list],
<                                              [state_labels],
<                                              circlabel)
---
>         if self._results is not None:
>             self._build_calibration_matrix()
75c75
<         return self._tens_fitt.cal_matrices[0]
---
>         return self._cal_matrix
80c80
<         self._tens_fitt.cal_matrices = [copy.deepcopy(new_cal_matrix)]
---
>         self._cal_matrix = new_cal_matrix
85c85
<         return self._tens_fitt.substate_labels_list[0]
---
>         return self._state_labels
95c95
<         self._tens_fitt.substate_labels_list[0] = new_state_labels
---
>         self._state_labels = new_state_labels
100,111c100
<         return MeasurementFilter(self.cal_matrix, self.state_labels)
< 
<     def add_data(self, new_results, rebuild_cal_matrix=True):
<         """
<         Add measurement calibration data
< 
<         Args:
<             new_results: a single result or list of results
<             rebuild_cal_matrix: rebuild the calibration matrix
<         """
< 
<         self._tens_fitt.add_data(new_results, rebuild_cal_matrix)
---
>         return MeasurementFilter(self._cal_matrix, self._state_labels)
126c115
<         if self._tens_fitt.cal_matrices is None:
---
>         if self._cal_matrix is None:
151c140
<         for label in self.state_labels:
---
>         for label in self._state_labels:
174c163
<                         new_cal_matrix[i, j] += self.cal_matrix[l, k]
---
>                         new_cal_matrix[i, j] += self._cal_matrix[l, k]
201c190,241
<         return self._tens_fitt.readout_fidelity(0, label_list)
---
> 
>         if self._cal_matrix is None:
>             raise QiskitError("Cal matrix has not been set")
> 
>         fidelity_label_list = []
>         if label_list is None:
>             fidelity_label_list = [[i] for i in range(len(self._cal_matrix))]
>         else:
>             for fid_sublist in label_list:
>                 fidelity_label_list.append([])
>                 for fid_statelabl in fid_sublist:
>                     for label_idx, label in enumerate(self._state_labels):
>                         if fid_statelabl == label:
>                             fidelity_label_list[-1].append(label_idx)
>                             continue
> 
>         # fidelity_label_list is a 2D list of indices in the
>         # cal_matrix, we find the assignment fidelity of each
>         # row and average over the list
>         assign_fid_list = []
> 
>         for fid_label_sublist in fidelity_label_list:
>             assign_fid_list.append(0)
>             for state_idx_i in fid_label_sublist:
>                 for state_idx_j in fid_label_sublist:
>                     assign_fid_list[-1] += \
>                         self._cal_matrix[state_idx_i][state_idx_j]
>             assign_fid_list[-1] /= len(fid_label_sublist)
> 
>         return np.mean(assign_fid_list)
> 
>     def _build_calibration_matrix(self):
>         """
>         Build the measurement calibration matrix from the results of running
>         the circuits returned by `measurement_calibration`
> 
>         Creates a 2**n x 2**n matrix that can be used to correct measurement
>         errors
>         """
> 
>         cal_matrix = np.zeros(
>             [len(self._state_labels), len(self._state_labels)], dtype=float)
> 
>         for stateidx, state in enumerate(self._state_labels):
>             state_cnts = self._results.get_counts('%scal_%s' %
>                                                   (self._circlabel, state))
>             shots = sum(state_cnts.values())
>             for stateidx2, state2 in enumerate(self._state_labels):
>                 cal_matrix[stateidx, stateidx2] = state_cnts.get(
>                     state2, 0) / shots
> 
>         self._cal_matrix = cal_matrix.transpose()
212c252,274
<         self._tens_fitt.plot_calibration(0, ax, show_plot)
---
>         if self._cal_matrix is None:
>             raise QiskitError("Cal matrix has not been set")
> 
>         if not HAS_MATPLOTLIB:
>             raise ImportError('The function plot_rb_data needs matplotlib. '
>                               'Run "pip install matplotlib" before.')
> 
>         if ax is None:
>             plt.figure()
>             ax = plt.gca()
> 
>         axim = ax.matshow(self._cal_matrix, cmap=plt.cm.binary, clim=[0, 1])
>         ax.figure.colorbar(axim)
>         ax.set_xlabel('Prepared State')
>         ax.xaxis.set_label_position('top')
>         ax.set_ylabel('Measured State')
>         ax.set_xticks(np.arange(len(self._state_labels)))
>         ax.set_yticks(np.arange(len(self._state_labels)))
>         ax.set_xticklabels(self._state_labels)
>         ax.set_yticklabels(self._state_labels)
> 
>         if show_plot:
>             plt.show()
239c301
<         self._result_list = []
---
>         self._results = results
262c324,325
<         self.add_data(results)
---
>         if self._results is not None:
>             self._build_calibration_matrices()
289,309d351
<     def add_data(self, new_results, rebuild_cal_matrix=True):
<         """
<         Add measurement calibration data
< 
<         Args:
<             new_results: a single result or list of results
<             rebuild_cal_matrix: rebuild the calibration matrix
<         """
< 
<         if new_results is None:
<             return
< 
<         if not isinstance(new_results, list):
<             new_results = [new_results]
< 
<         for result in new_results:
<             self._result_list.append(result)
< 
<         if rebuild_cal_matrix:
<             self._build_calibration_matrices()
< 
339,365c381,385
<         state_labels = self._substate_labels_list[cal_index]
<         fidelity_label_list = []
<         if label_list is None:
<             fidelity_label_list = [[label] for label in state_labels]
<         else:
<             for fid_sublist in label_list:
<                 fidelity_label_list.append([])
<                 for fid_statelabl in fid_sublist:
<                     for label_idx, label in enumerate(state_labels):
<                         if fid_statelabl == label:
<                             fidelity_label_list[-1].append(label_idx)
<                             continue
< 
<         # fidelity_label_list is a 2D list of indices in the
<         # cal_matrix, we find the assignment fidelity of each
<         # row and average over the list
<         assign_fid_list = []
< 
<         for fid_label_sublist in fidelity_label_list:
<             assign_fid_list.append(0)
<             for state_idx_i in fid_label_sublist:
<                 for state_idx_j in fid_label_sublist:
<                     assign_fid_list[-1] += \
<                         self._cal_matrices[cal_index][state_idx_i][state_idx_j]
<             assign_fid_list[-1] /= len(fid_label_sublist)
< 
<         return np.mean(assign_fid_list)
---
>         tmp_fitter = CompleteMeasFitter(None,
>                                         self._substate_labels_list[cal_index],
>                                         circlabel='')
>         tmp_fitter.cal_matrix = self.cal_matrices[cal_index]
>         return tmp_fitter.readout_fidelity(label_list)
380,408c400,421
<         for result in self._result_list:
<             for experiment in result.results:
<                 circ_name = experiment.header.name
<                 # extract the state from the circuit name
<                 # this was the prepared state
<                 circ_search = re.search('(?<=' + self._circlabel + 'cal_)\\w+',
<                                         circ_name)
< 
<                 # this experiment is not one of the calcs so skip
<                 if circ_search is None:
<                     continue
< 
<                 state = circ_search.group(0)
< 
<                 # get the counts from the result
<                 state_cnts = result.get_counts(circ_name)
<                 for measured_state, counts in state_cnts.items():
<                     end_index = self.nqubits
<                     for cal_ind, cal_mat in enumerate(self._cal_matrices):
< 
<                         start_index = end_index - \
<                             self._qubit_list_sizes[cal_ind]
< 
<                         substate_index = self._indices_list[cal_ind][
<                             state[start_index:end_index]]
<                         measured_substate_index = \
<                             self._indices_list[cal_ind][
<                                 measured_state[start_index:end_index]]
<                         end_index = start_index
---
>         for experiment in self._results.results:
>             circ_name = experiment.header.name
>             # extract the state from the circuit name
>             # this was the prepared state
>             state = re.search('(?<=' + self._circlabel + 'cal_)\\w+',
>                               circ_name).group(0)
> 
>             # get the counts from the result
>             state_cnts = self._results.get_counts(circ_name)
>             for measured_state, counts in state_cnts.items():
>                 end_index = self.nqubits
>                 for cal_ind, cal_mat in enumerate(self._cal_matrices):
> 
>                     start_index = end_index - \
>                         self._qubit_list_sizes[cal_ind]
> 
>                     substate_index = self._indices_list[cal_ind][
>                         state[start_index:end_index]]
>                     measured_substate_index = \
>                         self._indices_list[cal_ind][
>                             measured_state[start_index:end_index]]
>                     end_index = start_index
410,411c423,424
<                         cal_mat[measured_substate_index][substate_index] += \
<                             counts
---
>                     cal_mat[measured_substate_index][substate_index] += \
>                         counts
431,455c444,448
<         if self._cal_matrices is None:
<             raise QiskitError("Cal matrix has not been set")
< 
<         if not HAS_MATPLOTLIB:
<             raise ImportError('The function plot_rb_data needs matplotlib. '
<                               'Run "pip install matplotlib" before.')
< 
<         if ax is None:
<             plt.figure()
<             ax = plt.gca()
< 
<         axim = ax.matshow(self.cal_matrices[cal_index],
<                           cmap=plt.cm.binary,
<                           clim=[0, 1])
<         ax.figure.colorbar(axim)
<         ax.set_xlabel('Prepared State')
<         ax.xaxis.set_label_position('top')
<         ax.set_ylabel('Measured State')
<         ax.set_xticks(np.arange(len(self._substate_labels_list[cal_index])))
<         ax.set_yticks(np.arange(len(self._substate_labels_list[cal_index])))
<         ax.set_xticklabels(self._substate_labels_list[cal_index])
<         ax.set_yticklabels(self._substate_labels_list[cal_index])
< 
<         if show_plot:
<             plt.show()
---
>         tmp_fitter = CompleteMeasFitter(None,
>                                         self._substate_labels_list[cal_index],
>                                         circlabel='')
>         tmp_fitter.cal_matrix = self.cal_matrices[cal_index]
>         tmp_fitter.plot_calibration(ax, show_plot)
