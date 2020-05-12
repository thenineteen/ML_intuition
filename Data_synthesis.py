# Data Synthesis

def data_synthesis():
  X1 = np.array([
    [1, 1],
    ]* 100)
  X0 = np.array([
    [0, 0],
    ]* 100)
  X = np.concatenate([X0, X1])
  Xdf = pd.DataFrame(X)
  y1 = np.array([
    [1],
    ]* 100)
  y0 = np.array([
    [0],
    ]* 100)
  y = np.concatenate([y0, y1])
  
  # data label colours
  colours = pd.Series(['red']*100).append(pd.Series(['blue']*100))
  
  return X1, X0, X, Xdf, y1, y0, y, colours
