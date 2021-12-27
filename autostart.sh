#!/bin/bash

picom -b --config ~/.config/picom.conf
xinput disable "SynPS/2 Synaptics TouchPad"
nitrogen --restore

