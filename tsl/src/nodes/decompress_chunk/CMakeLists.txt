# Add all *.c to sources in upperlevel directory
set(SOURCES
    ${CMAKE_CURRENT_SOURCE_DIR}/batch_array.c
    ${CMAKE_CURRENT_SOURCE_DIR}/batch_queue_heap.c
    ${CMAKE_CURRENT_SOURCE_DIR}/batch_queue_fifo.c
    ${CMAKE_CURRENT_SOURCE_DIR}/compressed_batch.c
    ${CMAKE_CURRENT_SOURCE_DIR}/decompress_chunk.c
    ${CMAKE_CURRENT_SOURCE_DIR}/detoaster.c
    ${CMAKE_CURRENT_SOURCE_DIR}/exec.c
    ${CMAKE_CURRENT_SOURCE_DIR}/planner.c
    ${CMAKE_CURRENT_SOURCE_DIR}/pred_vector_array.c
    ${CMAKE_CURRENT_SOURCE_DIR}/qual_pushdown.c
    ${CMAKE_CURRENT_SOURCE_DIR}/vector_predicates.c)
target_sources(${TSL_LIBRARY_NAME} PRIVATE ${SOURCES})
