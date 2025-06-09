"use client";

import { useState } from "react";
import style from "./Checkbox.module.scss";

interface CheckboxProps {
    id: string;
    text: string;
    onChange?: () => void;
    checked?: boolean;
}

const Checkbox: React.FC<CheckboxProps> = ({
    id,
    onChange = () => {},
    text,
    checked = false,
}) => {
    const [isChecked, setIsChecked] = useState(checked);

    const handleChange = () => {
        setIsChecked(!isChecked);
        onChange();
    };

    return (
        <div className={style.checkbox_form}>
            <input
                type="checkbox"
                name={id}
                id={id}
                className="right-10"
                checked={isChecked}
                onChange={handleChange}
            />
            <label htmlFor={id} className="label-checkbox">
                {text}
            </label>
        </div>
    );
};

export default Checkbox;
