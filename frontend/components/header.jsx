import Link from "next/link";

import styles from "./header.module.css";

const Header = () => {
  return (
    <div className={styles.header_container}>
      <header>
        <Link href="/">ShaKyo!</Link>
      </header>
    </div>
  );
};

export default Header;
