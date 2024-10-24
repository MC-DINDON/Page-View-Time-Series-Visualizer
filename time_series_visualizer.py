import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns
from pandas.plotting import register_matplotlib_converters
register_matplotlib_converters()

# Import data (Make sure to parse dates. Consider setting index column to 'date'.)
df = pd.read_csv('fcc-forum-pageviews.csv', parse_dates=True, index_col=0)

# Clean data
q1 = (df['value'] >= df['value'].quantile(0.025))
q2 = (df['value'] <= df['value'].quantile(0.975))
df = df[q1&q2]


def draw_line_plot():
    df_line = df.copy()
    # Draw line plot
    x = df_line.index
    y = df_line.value
    fig, ax = plt.subplots(figsize=(16,5))
    plt.plot(x, y, color='red', linewidth=1)
    plt.xlabel("Date")  # add X-axis label
    plt.ylabel("Page Views")  # add Y-axis label
    plt.title("Daily freeCodeCamp Forum Page Views 5/2016-12/2019")

    # Save image and return fig (don't change this part)
    fig.savefig('line_plot.png')
    return fig

def draw_bar_plot():
    df_bar = df.copy()
    # Copy and modify data for monthly bar plot
    df_bar['year'], df_bar['month'] = df.index.year, df.index.month
    df_bar = df_bar.groupby(['year','month'],as_index=False).mean().round(0).astype(int)
    df_bar['month'] = pd.to_datetime(df_bar['month'], format='%m').dt.month_name()
    df_bar.rename(columns={"year":"Years","value":"Average Page Views","month":"Months"}, inplace = True)

    # Draw bar plot
    fig, ax = plt.subplots()

    chart = sns.barplot(data=df_bar, x="Years", y="Average Page Views", hue="Months", palette="tab10")
    # Save image and return fig (don't change this part)
    fig.savefig('bar_plot.png')
    return fig

def draw_box_plot():
    # Prepare data for box plots (this part is done!)
    df_box = df.copy()
    df_box.reset_index(inplace=True)
    df_box['year'] = [d.year for d in df_box.date]
    df_box['month'] = [d.strftime('%b') for d in df_box.date]

    # Draw box plots (using Seaborn)





    # Save image and return fig (don't change this part)
    fig.savefig('box_plot.png')
    return fig
