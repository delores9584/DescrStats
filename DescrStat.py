def DescrStat(datafile):
      data = np.loadtxt(datafile)
      data_mean = data.mean()
      data_std = data.std()
      data_var = data.var()

      print('Mean of the data is:', data_mean)
      print('Standard deviation of the data is:', data_std)
      print('Variance of the data is:', data_var)

      return data_mean, data_std, data_var