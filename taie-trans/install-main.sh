mvn install:install-file \
   -Dfile="$1" \
   -DgroupId=com.thealgorithms \
   -DartifactId=Java \
   -Dversion=1.0-SNAPSHOT \
   -Dpackaging=jar \
   -DgeneratePom=true

mvn install:install-file \
   -Dfile="$2" \
   -DgroupId=com.thealgorithms \
   -DartifactId=Java \
   -Dversion=1.0-SNAPSHOT \
   -Dpackaging=test-jar \
   -DgeneratePom=true
