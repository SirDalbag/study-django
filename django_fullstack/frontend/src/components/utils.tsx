export class Regex {
  static inputPassword(inputString: string): string {
    return inputString.replace(
      /[^a-zA-Z0-9@#$%^&*()_+{}\[\]:;<>,.?~\\/-]/g,
      ""
    );
  }
}

export class LocalStorage {
  static get(key: string) {
    try {
      const storedValue = localStorage.getItem(key);
      if (storedValue !== null) {
        return JSON.parse(storedValue);
      } else {
        return null;
      }
    } catch (error) {
      console.error(`error get localStorage: ${error}`);
      return null;
    }
  }
  static set(key: string, value: any) {
    try {
      localStorage.setItem(key, JSON.stringify(value));
    } catch (error) {
      console.error(`error set localStorage: ${error}`);
    }
  }

  static remove(key: string) {
    try {
      localStorage.removeItem(key);
    } catch (error) {
      console.error(`error remove localStorage: ${error}`);
    }
  }
}
