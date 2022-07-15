class PendudukThanos:

  def __init__(self, banyak_hari = 0):
    self.banyak_hari = banyak_hari
    self.penduduk = 1

  def muncul_dr_strange(self, penduduk = 1):
    penduduk *= 3
    return penduduk

  def muncul_thanos(self, penduduk = 1):
    penduduk //= 2
    return penduduk

  def hari_berjalan(self):
    if self.banyak_hari < 0:
        raise Exception("Error banyak hari tidak valid!")
    for hari in range(1, self.banyak_hari + 1, 1):
      if hari == 1:
        continue
      if (hari % 3) == 0:
        self.penduduk = self.muncul_thanos(self.penduduk)
        continue
      self.penduduk = self.muncul_dr_strange(self.penduduk)
    return self.penduduk
