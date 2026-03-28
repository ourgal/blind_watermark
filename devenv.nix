{ pkgs, ... }:
{
  languages.python = {
    enable = true;
    venv.enable = true;
    package = pkgs.python3.withPackages (ps: [
      ps.numpy
      ps.opencv-python
      ps.pywavelets
      ps.setuptools
    ]);
  };
}
