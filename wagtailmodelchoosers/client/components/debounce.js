function debounce(func, wait, immediate) {
  let timeout;
  let result;

  const later = (context, args) => {
    timeout = null;
    if (args) {
      result = func.apply(context, args);
    }
  };

  const debounced = (...args) => {
    const context = this;
    if (timeout) {
      clearTimeout(timeout);
    }
    if (immediate) {
      const callNow = !timeout;
      timeout = setTimeout(later, wait);
      if (callNow) {
        result = func.apply(context, args);
      }
    } else {
      timeout = setTimeout(later.bind(this, context, args), wait);
    }

    return result;
  };

  debounced.cancel = () => {
    clearTimeout(timeout);
    timeout = null;
  };

  return debounced;
}

export default debounce;