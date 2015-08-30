from __future__ import print_function
l=''
for d in '00d80c;0b<0a>0a>540a=2<0aJ0bJ0S99J0Q;;G0N><F0N>;E0HI583;0DW0AY0?]0>_0=a0<b0;d0;e0:>4@4D0:;453:353B0:;2927392A0;92:272:3@0;92;262;2@0;92;262;2@09;2;262;2B08<2:272;2D07>2928383E06A7<8G05p05p05p05p06n07l08k09i0:f0=a0AX00':
 if d=='0':
  print (l);f=0;l=''
 else:
  l+=("*"if f else" ")*(ord(d)-49);f=~f
