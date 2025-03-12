NXF_OPTS="-Xms500M -Xmx900M" NXF_DEFAULT_DSL=2 /usr/bin/time -v nextflow -c ADMIXTURE_Samoan_worldwide.config -bg run ADMIXTURE.nf -profile mccleary -w scratch 2> test.stderr > test.stdout

