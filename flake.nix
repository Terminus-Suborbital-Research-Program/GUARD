{
  description = "Tools and libraries for GUARD's Radiacode-103 Scintillator";

  inputs = {
    nixpkgs.url = "github:nixos/nixpkgs/nixos-25.05";
    flake-utils.url = "github:numtide/flake-utils";
  };

  outputs = { self, nixpkgs, flake-utils, ... }:
    flake-utils.lib.eachDefaultSystem (system:
      let
        pkgs = import nixpkgs { inherit system; };

        # Radiacode python packages
        radiacode = pkgs.callPackage ./packages/radiacode.nix { };
        radiaread =
          pkgs.callPackage ./packages/radiaread.nix { inherit radiacode; };

      in {
        packages = { inherit radiacode radiaread; };

        devShells.default =
          pkgs.mkShell { buildInputs = [ pkgs.python312 radiacode ]; };
      });
}
