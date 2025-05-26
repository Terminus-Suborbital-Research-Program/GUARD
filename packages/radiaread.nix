{ makeWrapper, stdenv, radiacode, python312Packages }:
let
  pname = "radiaread";
  version = "0.1.0";
in python312Packages.buildPythonApplication {
  inherit pname version;
  pyproject = false;

  propagatedBuildInputs = [ radiacode ];

  dontUnpack = true;
  installPhase = ''
    install -Dm755 ${./radiaread.py} $out/bin/radiaread
  '';

}
