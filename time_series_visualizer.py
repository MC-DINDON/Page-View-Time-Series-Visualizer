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
    month_order =  ['January', 'February', 'March', 'April', 'May', 'June', 'July', 'August', 'September', 'October', 'November', 'December'] 
    # Copy and modify data for monthly bar plot
    df_bar['year'], df_bar['month'] = df.index.year, df.index.month
    df_bar = df_bar.groupby(['year','month'],as_index=False).mean().round(0).astype(int)
    df_bar['month'] = pd.to_datetime(df_bar['month'], format='%m').dt.month_name()
    df_bar.rename(columns={"year":"Years","value":"Average Page Views","month":"Months"}, inplace = True)

    # Draw bar plot
    fig, ax = plt.subplots()

    chart = sns.barplot(data=df_bar, x="Years", y="Average Page Views", hue="Months",hue_order = month_order, palette="tab10")
    # Save image and return fig (don't change this part)
    fig.savefig('bar_plot.png')
    return fig

def draw_box_plot():
    # Prepare data for box plots (this part is done!)
    df_box = df.copy()
    df_box.reset_index(inplace=True)
    df_box['year'] = [d.year for d in df_box.date]
    df_box['month'] = [d.strftime('%b') for d in df_box.date]
    df_box.rename(columns = {"year":"Year", "month":"Month", "value": "Page Views"}, inplace=True)
    month_order =  ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec'] 

    # Draw box plots (using Seaborn)
    fig, ax = plt.subplots(1,2,figsize=(24,6))
    ygrph = sns.boxplot(data=df_box, x="Year", y="Page Views", hue="Year", palette="tab10",fliersize = 0.75, ax = ax[0])
    #warning! The object type will change from axes to text (cant apply some functions such as y limit then! Will name plot afterward)
    ygrph.set_ylim(0, 200000)
    ygrph.get_legend().remove()
    ygrph.set_title("Year-wise Box Plot (Trend)")

    mgrph = sns.boxplot(data=df_box, x="Month", y="Page Views", hue="Month",order = month_order, palette="tab10",fliersize = 0.75, ax = ax[1])
    #For some reason the .get_legend().remove() throws an error in the 2nd plot. 
    plt.legend([],[], frameon=False)
    mgrph.set_ylim(0, 200000)
    mgrph.get_legend().remove()
    mgrph.set_title("Month-wise Box Plot (Seasonality)")
    # Save image and return fig (don't change this part)
    plt.tight_layout()
    fig.savefig('box_plot.png')
    return fig
