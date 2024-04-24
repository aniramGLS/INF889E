from sklearn.decomposition import PCA
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
from sklearn.preprocessing import MinMaxScaler
from sklearn.preprocessing import StandardScaler


#################################
#####    DATA SCALING       #####
#################################

def normalization(X):
    """
    Normalization of the dataset
    """
    standardScaler = StandardScaler()
    
    return standardScaler.fit_transform(X)


##################################
#####     VISUALIZATION      #####
##################################

def generateScatterPlot(title, figure_width, figure_height, data, X, y, n_components):
    """
    Generate PCA visualization plot
    
    Keyword arguments:
    title -- Title of the graph
    figure_width, figure_height -- width and height size for the grapg
    data, X, y -- dataset
    n_components -- number of the component used for the analysis
    """
    # If 2d dimensions
    if n_components == 2:
        # Initialize a 2-dimensional figure
        fig, ax = plt.subplots(figsize=(figure_width, figure_height))
    # If 3d dimensions
    else:
        # Initialize a 3-dimensional figure
        fig = plt.figure(figsize=(15, 10))
        ax = Axes3D(fig)
    # List of markers
    markers = ["o","+", "^"]
    # List of colors
    colors = ["tab:blue", "tab:orange", 
              "tab:green", "tab:red", 
              "tab:purple", "tab:brown", 
              "tab:pink", "tab:grey", 
              "tab:olive", "tab:cyan",]
    
    # Iterate through the targets
    for i, target in enumerate(y):
        # Set the list of axis positions
        x = []
        y = []
        z = []
        # If the number of targets is less than 10
        if i < 10:
            color = colors[i]
            marker = markers[0]
        # If the number of targets is less than 20
        elif i < 20:
            color = colors[i-10]
            marker = markers[1]
        # If the number of targets is less than 30
        else:
            color = colors[i-20]
            marker = markers[2]
            
        # Iterate through the data
        for i, d in enumerate(data):
            # If the sequence belongs to the target of interest
            if d[2] == target:
                # Save the value of the positions
                x.append(X[i][0])
                y.append(X[i][1])
                if n_components == 3: z.append(X[i][2])
              
        # Add the current scatter plot to the figure
        if n_components == 2:
            ax.scatter(x, y, c = color, label = target, alpha = 0.75, edgecolors = 'none', marker=marker)
        else:
            ax.scatter(x, y, z, c = color, label=target,alpha=0.75, edgecolors='none', marker=marker)

    # Display the grid
    ax.grid(True)
    # Set the legend parameters
    ax.legend(loc = 2, prop = {'size': 10})
    # Set the tite
    plt.title(title)
    # Set axes labels
    if n_components == 2:
        plt.xlabel('PC1')
        plt.ylabel('PC2')
    else: 
        ax.set_xlabel('PC1')
        ax.set_ylabel('PC2')
        ax.set_zlabel('PC3')
    # Displqy the figure
    plt.savefig(f"PCA_transposable_{n_components}.png")

def run_pca(X_train, y_train, train_data):
    """
    Run PCA plot for training set and see data distribution
    
    Keyword arguments:
    X_train -- Kmer matrix
    y_train -- Superfamily matrix
    train_data -- Training dataset
    """
    pca = PCA(n_components = 2)
    X_pca =  pca.fit_transform(X_train)

    generateScatterPlot(title= "Scatter plot of a tree-dimensional PCA applied to the training data", 
                    figure_width = 15, 
                    figure_height = 12, 
                    data = train_data, 
                    X = X_pca, 
                    y = set(y_train), 
                    n_components = 2)
