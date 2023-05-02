226,232c226,230
<     gate_grid[0] = plot_params['labels_margin']
<     if depth > 0:
<         gate_grid[0] += width_list[0] * 0.5
<         for idx in range(1, depth):
<             gate_grid[idx] = gate_grid[idx - 1] + column_spacing + (
<                 width_list[idx] + width_list[idx - 1]) * 0.5
<         gate_grid[-1] = gate_grid[-2] + column_spacing + width_list[-1] * 0.5
---
>     gate_grid[0] = plot_params['labels_margin'] + (width_list[0]) * 0.5
>     for idx in range(1, depth):
>         gate_grid[idx] = gate_grid[idx - 1] + column_spacing + (
>             width_list[idx] + width_list[idx - 1]) * 0.5
>     gate_grid[-1] = gate_grid[-2] + column_spacing + width_list[-1] * 0.5
