from setuptools import find_packages, setup


def read_requirements():
    with open("requirements.txt", "r") as req:
        content = req.read()
        requirements = content.split("\n")

    return requirements


setup(
    name="BasketDataHub",
    version="0.1",
    packages=find_packages(),
    include_package_data=True,
    install_requires=read_requirements(),
    entry_points={
        'console_scripts': [
            'DataVisualization=DataVisualization.top20:indiv_stats',
            'DataVisualization=DataVisualization.boxes:home_overall_stats',
            'DataVisualization=DataVisualization.boxes:away_overall_stats',
            'DataVisualization=DataVisualization.histograms:hist_plot',
            'DataVisualization=DataVisualization.stats_comparison:indiv_player_df',
            # 'DataVisualization=DataVisualization.stats_comparison:get_stats',
        ],
    },
)
