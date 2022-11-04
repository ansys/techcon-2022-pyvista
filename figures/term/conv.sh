DIRECTORY=.

for i in termtosvg_*.svg; do
    google-chrome --headless --disable-gpu \
         --run-all-compositor-stages-before-draw \
         --print-to-pdf-no-header \
         --print-to-pdf="${i%.svg}.pdf" $i

done

