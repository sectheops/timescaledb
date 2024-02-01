cd timescaledb
   cmake -DCMAKE_BUILD_TYPE=Debug .
   make
   cd ..
   ./bootstrap -DCMAKE_BUILD_TYPE=Debug
   cd build && make
   ```
3. Run the test suite:
   ```bash
   make installcheck
