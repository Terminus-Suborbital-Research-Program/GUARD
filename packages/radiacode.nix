{ fetchFromGitHub, python312, python312Packages }:

let
  version = "0.3.5";
  pname = "radiacode";
in python312Packages.buildPythonPackage {

  inherit pname;

  nativeBuildInputs = with python312Packages; [ poetry-core ];

  dependencies = with python312Packages; [ pyusb bluepy ];

  inherit version;

  pyproject = true;

  src = fetchFromGitHub {
    owner = "cdump";
    repo = "radiacode";
    tag = version;
    sha256 = "sha256-BemaSVGlsOtdf/4LvPtAbmIwaQk5nxTsYSLli5D42BU=";
  };

  propogatedBuildInputs = with python312.pkgs; [ pyusb ];

  doCheck = true;
}
