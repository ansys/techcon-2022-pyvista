p = pv.Plotter()
p.add_mesh(starting_mesh, show_edges=True)
p.add_slider_widget(
    callback=callback,  # callable
    rng=[3, 60],
    value=30,
    title="Phi Resolution",
    pointa=(0.025, 0.1),
    pointb=(0.31, 0.1),
    style='modern',
)
