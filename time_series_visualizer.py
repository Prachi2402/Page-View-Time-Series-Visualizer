import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns
from pandas.plotting import register_matplotlib_converters

register_matplotlib_converters()

# Import data (Make sure to parse dates. Consider setting index column to 'date'.)
df = pd.read_csv('/work/fcc-forum-pageviews.csv', index_col='date', parse_dates=['date'])

# Clean data
df = df[(df.value > df.value.quantile(0.025)) & (df.value < df.value.quantile(0.975))]

def draw_line_plot():
    # Draw line plot

    fig, ax = plt.subplots(figsize=(10,5))
    ax.plot(df.index, df['value'], 'r', linewidth = 1)
    ax.set_title("Daily Freecode Forum Page Views 5/2016-12/2019")
    ax.set_xlabel("Date")
    ax.set_ylabel("Page Views")


    fig.savefig('line_plot.png')
    return fig

def draw_bar_plot():
    # Copy and modify data for monthly bar plot
    df_bar = df.copy()
    df['year'] = df.index.year
    df['month'] = df.index.month

    # grouping and orgenizing the df
    df_bar = df.groupby(['year', 'month'])['value'].mean()
    df_bar = df_bar.unstack

    # Draw bar plot
    fig = df_bar.plot.bar(figsize=(10,6), ylabel = "Average Page Views", xlabel = "Years").figure
    plt.legend(['January', 'February', 'March', 'April', 'May','June', 'July', 'August', 'September', 'October', 'November', 'December'])
    # plt.xlabel('Years');
    plt.xticks(fontsize = 8)
    plt.yticks(fontsize = 8)
    # plt.ylabel('Average Page Views');
    # plt.legend(title='Months');

    # Save image and return fig (don't change this part)
    fig.savefig('bar_plot.png')
    return fig

def draw_box_plot():
    # Prepare data for box plots (this part is done!)
    df_box = df.copy()
    df_box.reset_index(inplace=True)
    df_box['year'] = [d.year for d in df_box.date]
    df_box['month'] = [d.strftime('%b') for d in df_box.date]

    mon_order = ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec']

    # Draw box plots (using Seaborn)
    # fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(20, 5))

    df_box["month_num"] = df_box["date"].dt.month
    df_box = df_box.sort_values["month_num"]

    fig, axes = plt.subplots(nrows = 1, ncols = 2, figsize=(10, 5))
    axes[0]=sns.boxplot(x=df_box["year"], y =df_box["value"], ax = axes[0]) 
   axes[0]=sns.boxplot(x=df_box["month"], y =df_box["value"], ax = axes[1])
    axes[0].set_title('Year-wise box plot (Trend)')
    axes[0].set_xlabel('Year')
    axes[0].set_ylabel('Page Views')

    axes[1].set_title('Month-wise box plot (Seasonality)')
    axes[1].set_xlabel('Month')
    axes[1].set_ylabel('Page Views')

    # Save image and return fig (don't change this part)
    fig.savefig('box_plot.png')
    return fig
