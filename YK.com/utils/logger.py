import logging

logger = logging.getLogger("test_logger")
logger.setLevel(logging.INFO)

def setup_logger(log_file_path):
    handler = logging.FileHandler(log_file_path, encoding='utf-8')
    formatter = logging.Formatter('%(asctime)s | %(message)s', "%H:%M:%S")
    handler.setFormatter(formatter)
    logger.addHandler(handler)

def log_test_info(test_name, status, duration, comment):
    msg = f"{test_name} | Статус: {status.upper()} | Время: {duration:.2f}s | Комментарий: {comment}"
    logger.info(msg)
